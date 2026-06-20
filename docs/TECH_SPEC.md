# TECH_SPEC.md
**Project:** admin‑bootcamp  
**Owner:** Axentx – Product Engineering  
**Status:** MVP – Ready for development sprint  

---  

## 1. Overview  

admin‑bootcamp is a **structured learning platform for system‑administration**.  
It delivers beginner‑friendly modules, interactive labs, and a clear learning path that tracks progress, awards badges, and surfaces next‑step recommendations.  

The system is built as a **modular, cloud‑native web application** with a clear separation between:

| Layer | Responsibility |
|-------|-----------------|
| **Presentation** | React SPA (Next.js) – UI, routing, client‑side state |
| **Application** | FastAPI (Python 3.11) – REST/GraphQL API, business logic |
| **Data** | PostgreSQL (14) – relational store for users, courses, progress, lab environments |
| **Infrastructure** | Docker + Helm → Kubernetes (GKE/EKS) – scalable, zero‑downtime deployments |
| **Observability** | Prometheus + Grafana, Loki for logs, OpenTelemetry tracing |
| **CI/CD** | GitHub Actions → Docker Build → ArgoCD (GitOps) |

---  

## 2. Architecture Diagram  

```
+-------------------+        +-------------------+        +-------------------+
|   Browser (SPA)   | <----> |   API Gateway     | <----> |   FastAPI Service |
|  (Next.js/React)  |        | (Envoy)           |        | (Python)          |
+-------------------+        +-------------------+        +-------------------+
                                   |   ^                     |
                                   |   |                     |
                                   v   |                     v
                           +-------------------+   +-------------------+
                           |  Auth Service     |   |  Course Service   |
                           | (Keycloak OIDC)   |   | (FastAPI modules) |
                           +-------------------+   +-------------------+
                                   |                     |
                                   v                     v
                           +-----------------------------------+
                           |          PostgreSQL Cluster        |
                           |  (users, courses, progress, labs) |
                           +-----------------------------------+
                                   |
                                   v
                           +-------------------+
                           |  Lab Orchestrator |
                           | (Docker‑in‑Docker |
                           |  + Terraform)     |
                           +-------------------+
```

*All services run as Docker containers, deployed via Helm charts.*  

---  

## 3. Core Components  

| Component | Description | Tech / Libs |
|-----------|-------------|-------------|
| **Frontend** | Next.js SPA with server‑side rendering for SEO, dynamic routing per learning path, offline caching via Service Worker. | React 18, Next.js 14, TypeScript, TailwindCSS, SWR, i18next |
| **API Gateway** | Envoy proxy handling TLS termination, request routing, rate‑limiting, and JWT validation. | Envoy 1.28, OpenID Connect |
| **Auth Service** | Central identity provider; supports SSO (Google, GitHub) and email/password. Issues short‑lived access tokens and refresh tokens. | Keycloak 23, OIDC, bcrypt |
| **FastAPI Core** | Main backend exposing both **REST** (for admin UI) and **GraphQL** (for SPA). Handles user profile, enrollment, progress, badge issuance. | FastAPI, Pydantic, Strawberry GraphQL, Uvicorn, Gunicorn |
| **Course Service** | Manages course metadata, module ordering, lab definitions (Docker compose files). Provides versioned content via Git‑backed storage. | SQLAlchemy 2.0, Alembic, GitPython |
| **Lab Orchestrator** | Spins up isolated lab environments per user (Docker containers with privileged‑mode networking). Labs are defined as Docker‑Compose templates stored in the repo. | Docker SDK for Python, Terraform (for cloud resources), netns, cgroups |
| **Data Store** | Relational DB with logical separation via schemas: `public` (auth), `learning` (courses, progress), `labs` (lab instance metadata). | PostgreSQL 14, pg_partman for time‑based partitioning |
| **Observability** | Metrics, logs, and traces exported to Prometheus/Grafana stack. | Prometheus client, OpenTelemetry SDK, Loki, Grafana dashboards |
| **CI/CD** | Automated lint, unit/integration tests, container build, Helm chart lint, and promotion to staging/production via ArgoCD. | GitHub Actions, Docker Buildx, Helm, ArgoCD |

---  

## 4. Data Model  

### 4.1 ER Diagram (simplified)

```
User ──< Enrollment >── Course ──< Module >── LabDefinition
 │                                 │
 └─< Progress >─────────────────────┘
```

### 4.2 Key Tables  

| Table | Columns | Description |
|-------|---------|-------------|
| `users` | `id PK`, `email`, `hashed_pwd`, `full_name`, `created_at`, `last_login` | Identity data (Keycloak sync). |
| `courses` | `id PK`, `slug`, `title`, `description`, `level`, `published_at` | Top‑level learning tracks. |
| `modules` | `id PK`, `course_id FK`, `order`, `title`, `content_md`, `lab_def_id FK` | Individual lessons. |
| `lab_definitions` | `id PK`, `name`, `docker_compose_yaml`, `timeout_secs` | Template for a lab environment. |
| `enrollments` | `id PK`, `user_id FK`, `course_id FK`, `started_at`, `completed_at` | User‑course relationship. |
| `progress` | `id PK`, `enrollment_id FK`, `module_id FK`, `status ENUM('not_started','in_progress','completed')`, `started_at`, `completed_at` | Per‑module progress. |
| `badges` | `id PK`, `user_id FK`, `name`, `earned_at` | Gamification. |
| `lab_instances` | `id PK`, `user_id FK`, `lab_def_id FK`, `container_id`, `host_port`, `status ENUM('running','stopped','failed')`, `created_at`, `expires_at` | Live lab containers. |

All tables use **UTC timestamps** and have appropriate indexes (e.g., `user_id`, `course_id`, `status`).  

---  

## 5. API Specification  

### 5.1 Authentication (REST)  

| Method | Path | Auth | Request | Response |
|--------|------|------|---------|----------|
| POST | `/api/v1/auth/login` | – | `{email, password}` | `{access_token, refresh_token, expires_in}` |
| POST | `/api/v1/auth/refresh` | Refresh token | `{refresh_token}` | `{access_token, expires_in}` |
| POST | `/api/v1/auth/logout` | Bearer | – | `204 No Content` |

### 5.2 GraphQL Endpoint  

`POST /graphql` – JWT Bearer token required.  
Schema (excerpt):

```graphql
type Query {
  me: User!
  courses: [Course!]!
  course(slug: String!): Course
  enrollment(courseSlug: String!): Enrollment
}

type Mutation {
  enroll(courseSlug: String!): Enrollment!
  startModule(moduleId: ID!): Progress!
  completeModule(moduleId: ID!): Progress!
  launchLab(labDefId: ID!): LabInstance!
  stopLab(labInstanceId: ID!): Boolean!
}
```

### 5.3 Lab Management (REST)  

| Method | Path | Auth | Request | Response |
|--------|------|------|---------|----------|
| POST | `/api/v1/labs/{labDefId}/launch` | Bearer | `{}` | `{labInstanceId, url, expiresAt}` |
| POST | `/api/v1/labs/{labInstanceId}/stop` | Bearer | – | `{stopped: true}` |
| GET  | `/api/v1/labs/{labInstanceId}/status` | Bearer | – | `{status, createdAt, expiresAt}` |

All responses follow **JSON:API** conventions (data, meta, errors).  

---  

## 6. Technology Stack  

| Layer | Choice | Rationale |
|-------|--------|-----------|
| Frontend | **Next.js 14** (React 18, TypeScript) | SEO‑friendly, incremental static regeneration for course pages, excellent developer DX. |
| Backend | **FastAPI** (Python 3.11) | High performance, async support, automatic OpenAPI docs, easy Pydantic validation. |
| API Gateway | **Envoy** | Industry‑standard, supports gRPC/REST, easy to extend with filters. |
| Auth | **Keycloak** | Open‑source OIDC provider, supports social login, LDAP, fine‑grained roles. |
| DB | **PostgreSQL 14** | ACID guarantees, rich JSONB support for flexible content fields. |
| Lab Runtime | **Docker‑in‑Docker** + **Terraform** | Guarantees isolation per user, reproducible environments, can be swapped for Kubernetes Pods in future. |
| Container Runtime | **Docker Engine 24** | Widely available on cloud VMs, simple CLI for lab orchestration. |
| Orchestration | **Kubernetes (GKE/EKS)** | Horizontal scaling, auto‑healing, secret management. |
| CI/CD | **GitHub Actions** + **ArgoCD** | GitOps flow, automatic promotion after integration tests. |
| Monitoring | **Prometheus + Grafana**, **Loki**, **OpenTelemetry** | Full observability stack, ready for multi‑tenant dashboards. |
| Packaging | **Helm 3** charts per service | Versioned, reusable deployments. |

---  

## 7. Dependencies  

| Dependency | Version | License |
|------------|---------|---------|
| python | >=3.11,<3.12 | PSF |
| fastapi | 0.110.0 | MIT |
| uvicorn | 0.27.0 | BSD-3 |
| sqlalchemy | 2.0.30 | MIT |
| alembic | 1.13.1 | MIT |
| strawberry-graphql | 0.221.0 | BSD-3 |
| keycloak-admin | 0.13.0 | Apache‑2.0 |
| docker (SDK) | 7.1.0 | Apache‑2.0 |
| terraform | 1.9.5 | MPL‑2.0 |
| next | 14.2.0 | MIT |
| react | 18.2.0 | MIT |
| tailwindcss | 3.4.0 | MIT |
| envoy | 1.28.x | Apache‑2.0 |
| prometheus-client | 0.20.0 | Apache‑2.0 |
| opentelemetry-sdk | 1.24.0 | Apache‑2.0 |

All third‑party libraries are vetted for **commercial permissive licenses** (MIT, Apache‑2.0, BSD).  

---  

## 8. Deployment Architecture  

### 8.1 Environments  

| Env | Namespace | DB | Domain | Notes |
|-----|-----------|----|--------|-------|
| Development | `admin-bootcamp-dev` | PostgreSQL‑dev (single node) | dev.admin-bootcamp.axentx.io | Auto‑deploy on PR merge to `dev`. |
| Staging | `admin-bootcamp-stg` | PostgreSQL‑stg (HA) | stg.admin-bootcamp.axentx.io | Runs integration test suite nightly. |
| Production | `admin-bootcamp-prod` | PostgreSQL‑prod (regional HA) | admin-bootcamp.axentx.io | Zero‑downtime rollouts via ArgoCD. |

### 8.2 Helm Chart Structure  

```
admin-bootcamp/
├─ charts/
│  ├─ frontend/
│  ├─ api-gateway/
│  ├─ auth/
│  ├─ backend/
│  └─ lab-orchestrator/
└─ values/
   ├─ dev.yaml
   ├─ stg.yaml
   └─ prod.yaml
```

Each chart defines:

* Deployment (replicas, resources, liveness/readiness probes)  
* Service (ClusterIP + Ingress)  
* ConfigMap for environment variables (feature flags, URLs)  
* Secret references (DB credentials, JWT secret)  

### 8.3 CI/CD Flow  

1. **Push** → GitHub Action runs lint + unit tests.  
2. **Docker Build** → Multi‑arch image (`linux/amd64,linux/arm64`).  
3. **Push** to GCR/AR (`<env>-admin-bootcamp-frontend:sha`).  
4. **ArgoCD** watches `helm/values/<env>.yaml`; on image tag change it performs a **helm upgrade** with `--atomic`.  
5. Post‑deploy **smoke tests** (k6) run; failures block promotion.  

---  

## 9. Security Considerations  

| Area | Controls |
|------|----------|
| **Authentication** | OIDC with short‑lived JWTs (15 min) + refresh tokens (7 days). Tokens signed with RS256 using Keycloak keys. |
| **Authorization** | Role‑based ACL (admin, instructor, learner). Enforced in FastAPI dependencies. |
| **Transport** | All ingress via TLS 1.3 (managed by Cloud Load Balancer). Envoy terminates TLS. |
| **Data at Rest** | PostgreSQL encrypted with Cloud KMS. Docker volumes for labs encrypted via `dm-crypt`. |
| **Lab Isolation** | Each lab runs in its own Docker container with limited capabilities (`--cap-drop ALL`, user‑ns). Network is NAT‑ed; no inbound ports. |
| **Secrets Management** | Kubernetes Secrets stored encrypted with SealedSecrets; accessed via env vars only. |
| **Vulnerability Scanning** | Trivy scan on each image; CI fails on CVE > 7. |
| **Rate Limiting** | Envoy limits to 100 req/s per IP; login endpoint limited to 5 attempts/ minute. |

---  

## 10. Observability & Alerting  

* **Metrics** – Prometheus scrapes `/metrics` from FastAPI, Envoy, and lab‑orchestrator.  
* **Dashboards** – Grafana dashboards for: API latency, error rates, lab container count, DB connection pool.  
* **Logs** – Structured JSON logs shipped to Loki via Fluent Bit.  
* **Tracing** – OpenTelemetry instrumentation across request flow (frontend → gateway → backend → lab).  
* **Alerts** – PrometheusRule alerts for: >5% 5xx errors, DB connection >80% utilization, lab spawn failures >2/min.  

---  

## 11. Testing Strategy  

| Test Type | Scope | Tools |
|-----------|-------|-------|
| Unit | Pure functions, Pydantic models, service helpers | pytest, hypothesis |
| Integration | API endpoints + DB (test container) | pytest‑asyncio, testcontainers‑postgres |
| End‑to‑End | Full user journey (login → enroll → launch lab) | Playwright (Chromium) |
| Load | Simulated concurrent learners (10k) | k6, Locust |
| Security | OWASP ZAP scan, dependency CVE audit | ZAP, Trivy, bandit |
| Contract | OpenAPI spec validation against implementation | schemathesis |

All tests run in CI; coverage target **≥ 85 %**.  

---  

## 12. Release & Versioning  

* **Semantic Versioning** – `MAJOR.MINOR.PATCH`.  
* **Changelog** – Auto‑generated from PR titles (conventional commits).  
* **Rollback** – Helm `--revision` rollback; Docker images immutable (sha tags).  

---  

## 13. Open Issues & Future Work  

| Issue | Description | Owner | Target Sprint |
|-------|-------------|-------|---------------|
| Lab Scaling | Replace Docker‑in‑Docker with per‑lab Kubernetes Pods for better multi‑tenant scaling. | Infra Lead | Sprint 5 |
| Content Authoring UI | Build a markdown‑based CMS for instructors (WYSIWYG). | Product | Sprint 3 |
| Offline Mode | Service‑worker caching for read‑only content. | Frontend | Sprint 4 |
| Multi‑Language Support | i18n for Spanish & Mandarin. | Localization | Sprint 6 |

---  

**Prepared by:** Senior Product/Engineering Lead – admin‑bootcamp  
**Date:** 2026‑06‑20  

---
