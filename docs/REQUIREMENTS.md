# REQUIREMENTS.md
**Project:** admin-bootcamp  
**Owner:** AxentX – Product Engineering  
**Date:** 2026‑06‑20  
**Version:** 1.0  

---  

## 1. Overview  

admin‑bootcamp is a structured, web‑based learning platform that teaches system‑administration fundamentals to beginners. It delivers curated learning paths, interactive labs, assessments, and progress tracking. The product must be **pay‑ready**, **scalable**, and **secure**, fitting within AxentX’s existing technology stack (React, Node.js, PostgreSQL, Docker, and the vLLM inference engine for AI‑generated hints).  

---  

## 2. Functional Requirements  

| ID | Description |
|----|-------------|
| **FR‑1** | **User Registration & Authentication** – Users can sign‑up with email/password or SSO (Google, GitHub). Passwords are stored using Argon2id. Email verification is mandatory before access to any content. |
| **FR‑2** | **Role Management** – Three roles: **Learner**, **Instructor**, **Admin**. Role‑based access control (RBAC) governs UI visibility and API permissions. |
| **FR‑3** | **Learning Paths** – Admins can create, edit, reorder, and retire *Learning Paths* composed of ordered *Modules*. Each Module contains: <br>• Title & description <br>• Optional video (YouTube embed or uploaded MP4) <br>• Markdown content (theory) <br>• Interactive lab (Docker‑based sandbox) <br>• Quiz (multiple‑choice & short‑answer). |
| **FR‑4** | **Progress Tracking** – The system records per‑user: <br>• Completed Modules <br>• Quiz scores <br>• Lab success/failure <br>• Time spent per Module. A visual progress bar is displayed on the dashboard. |
| **FR‑5** | **Interactive Labs** – When a learner starts a lab, a isolated Docker container is provisioned on the Lab‑Runner service. The container runs a minimal Linux distro with pre‑installed tools (bash, ssh, systemd, networking utilities). Learners interact via an in‑browser terminal (xterm.js). Lab state is persisted for the duration of the session (max 2 h). |
| **FR‑6** | **AI‑Assisted Hints** – While a learner is in a lab, they can request a context‑aware hint. The request is sent to the vLLM inference service, which returns a concise, safety‑filtered suggestion. |
| **FR‑7** | **Assessments & Certification** – After completing a Learning Path, the learner must pass a final assessment (minimum 80 % score). Upon success, a PDF certificate (signed with the company’s private key) is generated and emailed. |
| **FR‑8** | **Admin Dashboard** – Admins can: <br>• View platform analytics (user sign‑ups, completion rates, average quiz scores). <br>• Manage users (activate, suspend, role change). <br>• Moderate forum posts (see FR‑9). |
| **FR‑9** | **Community Forum (Optional MVP)** – Learners can post questions and answers related to a Module. Posts are markdown‑rendered, can be up‑voted, and are moderated by Instructors. |
| **FR‑10** | **Payment Integration (Future‑Ready)** – The platform must expose a **“Purchase Path”** endpoint that can be wired to Stripe/PayPal. For the MVP, the endpoint returns a stub success response; the integration will be completed in a later release. |
| **FR‑11** | **API First** – All UI actions are backed by a versioned RESTful JSON API (`/api/v1/...`). The API is documented with OpenAPI 3.0 and includes authentication via JWT. |
| **FR‑12** | **Internationalisation (i18n) Ready** – All UI strings are externalised; the platform ships with English and Spanish locales. Adding new locales must not require code changes. |

---  

## 3. Non‑Functional Requirements  

| ID | Category | Requirement |
|----|----------|-------------|
| **NFR‑1** | **Performance** | • API latency ≤ 200 ms for 95 % of requests under load of 500 concurrent users. <br>• Lab container start‑up time ≤ 5 s. |
| **NFR‑2** | **Scalability** | • Stateless front‑end and API services; horizontal scaling via Kubernetes. <br>• Lab‑Runner service must support auto‑scaling of container pods based on queue length. |
| **NFR‑3** | **Security** | • All traffic encrypted (TLS 1.3). <br>• OWASP Top 10 mitigations (SQLi, XSS, CSRF, etc.). <br>• JWT tokens signed with RSA‑4096, rotated every 24 h. <br>• Lab containers run with non‑root user, limited capabilities, and network isolation (no outbound internet). |
| **NFR‑4** | **Reliability** | • 99.9 % uptime SLA (excluding scheduled maintenance). <br>• Automated backups of PostgreSQL (hourly) and lab container images (daily). <br>• Graceful degradation: if AI‑hint service is unavailable, UI shows “Hint unavailable – try again later”. |
| **NFR‑5** | **Observability** | • Centralised logging (ELK stack) with correlation IDs. <br>• Metrics exposed via Prometheus (request latency, error rates, lab container count). <br>• Alerts for error‑rate > 2 % or CPU > 80 % on any pod. |
| **NFR‑6** | **Maintainability** | • Codebase follows AxentX linting and formatting rules. <br>• Unit test coverage ≥ 80 % for core services; integration tests for API endpoints ≥ 70 %. <br>• CI/CD pipeline (GitHub Actions) runs lint, test, build, and deploy on every PR merge. |
| **NFR‑7** | **Compliance** | • GDPR‑compliant data handling (right‑to‑be‑forgotten endpoint). <br>• Accessibility: WCAG 2.1 AA compliance for UI components. |
| **NFR‑8** | **Data Privacy** | • No learner data is sent to external services except optional AI‑hint request payloads, which are stripped of personally identifiable information. |
| **NFR‑9** | **Portability** | • All services containerised (Docker) and orchestrated with Helm charts. Must run on any Kubernetes 1.27+ cluster (AWS EKS, GKE, Azure AKS). |

---  

## 4. Constraints  

1. **Technology Stack** – Must use the existing AxentX stack:  
   * Front‑end: React 18 + TypeScript + TailwindCSS.  
   * Back‑end: Node.js 20 (Express) + PostgreSQL 15.  
   * Container orchestration: Kubernetes (Helm).  
   * AI hint service: vLLM (already deployed in the company’s inference cluster).  

2. **Data Residency** – All user‑generated data (progress, quiz answers) must reside in EU‑hosted PostgreSQL clusters to satisfy GDPR.  

3. **Budget** – Initial MVP must stay within the “boot‑strap” budget: ≤ $12,000/month for cloud resources (compute, storage, bandwidth).  

4. **Release Timeline** – MVP (core learning path, labs, progress tracking, AI hints) must be production‑ready within **12 weeks** from project kickoff.  

5. **No Duplicate Functionality** – The product must not replicate existing AxentX offerings (e.g., the “iceoryx2” training module). Any shared components (auth, UI library) must be reused, not re‑implemented.  

---  

## 5. Assumptions  

| ID | Assumption |
|----|------------|
| **A‑1** | The vLLM inference endpoint is already provisioned and reachable at `https://inference.axentx.internal/v1/hint`. |
| **A‑2** | A Lab‑Runner service (Docker‑in‑Docker) exists and exposes a REST API for container lifecycle (`/labs/create`, `/labs/attach`, `/labs/terminate`). |
| **A‑3** | User email delivery (SMTP) is handled by the company‑wide mail service; the platform only needs to call its API. |
| **A‑4** | Content authors will provide Markdown files and optional media assets via the admin UI; no external content‑authoring tool is required for MVP. |
| **A‑5** | The product will launch initially in English; Spanish localisation will be a parallel effort but not a gating factor for MVP release. |
| **A‑6** | All third‑party libraries used are compatible with the company’s open‑source license policy (MIT, Apache‑2.0, BSD). |
| **A‑7** | The target audience has broadband internet ≥ 10 Mbps, sufficient for video streaming and interactive labs. |

---  

## 6. Acceptance Criteria (High‑Level)  

1. A new learner can register, verify email, and start a Learning Path within 2 minutes.  
2. An instructor can create a Learning Path with at least 3 Modules, each containing theory, a lab, and a quiz, and publish it.  
3. A learner can complete a lab, request an AI hint, and see the hint within 1 second of request (excluding network latency).  
4. Progress is persisted across devices and reflected accurately on the dashboard.  
5. Admins can view real‑time analytics and export a CSV of user completion data.  
6. All security tests (OWASP ZAP, dependency scanning) pass with no critical findings.  

---  

*Prepared by:* Senior Product/Engineering Lead – admin‑bootcamp  
*Reviewed by:* Architecture Review Board, Security Team, QA Lead  

---
