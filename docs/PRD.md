# 📄 Product Requirements Document (PRD)  
**Project:** admin-bootcamp  
**Owner:** Senior Product/Engineering Lead – Axentx  
**Date:** 2026‑06‑20  
**Status:** Draft → Review → Approved → Execution  

---  

## 1. Problem Statement  

System administrators (SysAdmins) are essential for modern cloud‑native enterprises, yet there is a **significant skills gap**:

* New hires and career‑switchers struggle to find a **structured, hands‑on learning path** that covers both classic Unix administration and modern infrastructure‑as‑code (IaC) tooling.  
* Existing resources are fragmented (blog posts, video tutorials, vendor docs) and lack **progress tracking**, **skill validation**, and **real‑world lab environments**.  
* Companies spend **30‑45 %** of onboarding time on ad‑hoc training, leading to slower incident response and higher operational risk.

**admin‑bootcamp** will close this gap by delivering a **guided, competency‑based learning platform** for system administration, from fundamentals to production‑grade cloud operations.

---  

## 2. Target Users  

| Segment | Persona | Primary Pain Points | Desired Outcome |
|---------|---------|---------------------|-----------------|
| **A. Junior SysAdmins / Career‑Switchers** | “Alex” – recent CS graduate, 0‑2 yr experience | No clear curriculum, limited lab access, no certification | Gain job‑ready skills, earn a verifiable badge |
| **B. Mid‑level Ops Engineers** | “Sam” – 3‑5 yr experience, moving to cloud‑native | Need to upskill on IaC, containers, observability | Structured refresher, micro‑credential for new tech |
| **C. Enterprise L&D Teams** | “Maya” – Learning manager at a mid‑size SaaS firm | High onboarding cost, inconsistent training quality | Deploy a ready‑made curriculum, track team progress |

---  

## 3. Goals & Success Metrics  

| Goal | Metric | Target (12 mo) |
|------|--------|----------------|
| **G1. Market Validation** – Demonstrate paying demand | # of paid pilot customers (enterprise L&D) | ≥ 5 |
| **G2. User Adoption** – Build an engaged learner base | Active learners (≥ 1 hr/week) | ≥ 2,000 |
| **G3. Skill Validation** – Provide measurable outcomes | Completion + badge issuance rate | ≥ 70 % of enrolled learners |
| **G4. Revenue Generation** – Reach revenue‑validated product status | Monthly Recurring Revenue (MRR) | $45 k |
| **G5. Platform Stability** – Ensure production‑grade experience | 99.5 % uptime, < 2 s page load | ≥ 99.5 % uptime, < 2 s avg. load |

---  

## 4. Scope  

### 4.1 In‑Scope (MVP)  

| Priority | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|----------------------|
| **P1** | **Learning Path Engine** | Curated curriculum broken into modules → lessons → labs. Supports prerequisite logic. | • Admin can create/edit paths via UI.<br>• Learner sees next recommended lesson automatically. |
| **P2** | **Interactive Lab Environment** | Browser‑based, containerized sandbox (Docker + K8s) with pre‑installed tools (bash, systemd, Ansible, Terraform, Prometheus). | • Lab spins up ≤ 10 s.<br>• Learner can execute commands, view file system, and reset. |
| **P3** | **Progress & Assessment Dashboard** | Visual progress bar, quiz scores, lab completion status, badge issuance. | • Learner can view real‑time progress.<br>• Badge generated on 80 %+ overall score. |
| **P4** | **Content Authoring UI** | Markdown‑based lesson editor with code block execution preview. | • Non‑technical admin can publish a lesson in < 15 min. |
| **P5** | **Subscription & Billing** | Tiered plans: Free (core path), Pro (full catalog + certificates), Enterprise (SSO, team analytics). | • Payment flow via Stripe succeeds.<br>• License enforcement per tier. |
| **P6** | **Analytics & Reporting** | Admin view of cohort performance, drop‑off points, time‑on‑task. | • Exportable CSV/JSON reports. |
| **P7** | **Accessibility & Internationalization** | WCAG 2.1 AA compliance, UI strings externalized for i18n (English + Spanish). | • Automated aXe audit passes. |

### 4.2 Out‑of‑Scope (Post‑MVP)  

| Feature | Reason for Deferral |
|---------|---------------------|
| Live instructor‑led sessions | Will be added as premium add‑on after market traction. |
| AI‑generated personalized hints (LLM‑driven) | Requires additional model serving infra; slated for Q3‑2027. |
| Mobile native app | Web‑responsive UI sufficient for MVP; native app planned after user growth. |
| Integration with external certification bodies | Initial badge is internal; partnership roadmap later. |
| Multi‑cloud lab orchestration (AWS/GCP/Azure) | MVP uses a single Kubernetes cluster; expand in Phase 2. |

---  

## 5. Functional Requirements  

| ID | Requirement | Type | Priority |
|----|-------------|------|----------|
| FR‑001 | Curriculum editor must enforce prerequisite DAG integrity. | Functional | P1 |
| FR‑002 | Lab containers must be isolated per user, with auto‑cleanup after 30 min idle. | Functional | P2 |
| FR‑003 | Quiz engine supports multiple‑choice, fill‑in‑the‑blank, and code‑output validation. | Functional | P3 |
| FR‑004 | Badge metadata stored in immutable ledger (pgvector) for verification. | Functional | P3 |
| FR‑005 | Subscription API must expose `GET /plan`, `POST /subscribe`, `GET /status`. | Functional | P5 |
| FR‑006 | Export reports in CSV with columns: learner_id, module, score, time_spent. | Functional | P6 |
| FR‑007 | UI must be responsive down to 320 px width. | Non‑functional | P7 |
| FR‑008 | System must handle concurrent labs for 500 users with < 2 s latency. | Performance | P2 |
| FR‑009 | All data at rest encrypted (AES‑256) and in‑transit TLS 1.3. | Security | P5 |
| FR‑010 | Audit log of content changes retained 12 months. | Compliance | P1 |

---  

## 6. Technical Architecture (High‑Level)  

* **Frontend:** React 18 + TypeScript, TailwindCSS, React‑Router.  
* **Backend API:** FastAPI (Python 3.11) – handles curriculum, auth, billing.  
* **Auth:** OAuth2 + OpenID Connect (supports SSO via SAML for Enterprise).  
* **Lab Orchestration:** vLLM‑compatible container pool managed by **SGLang** for structured command execution; each lab runs in a lightweight Docker container on a shared K8s cluster.  
* **Data Store:** PostgreSQL 15 (core data) + pgvector extension for embedding‑based search of lessons.  
* **Billing:** Stripe Connect integration.  
* **CI/CD:** GitHub Actions → Docker Build → ArgoCD to staging/production clusters.  
* **Observability:** Prometheus + Grafana dashboards; Loki for logs.  

---  

## 7. Milestones & Timeline  

| Milestone | Deliverable | Owner | Target Date |
|-----------|-------------|-------|-------------|
| **M1** | Requirements sign‑off (this PRD) | PM / Lead | 2026‑06‑28 |
| **M2** | Architecture & tech‑stack freeze | Architecture Lead | 2026‑07‑05 |
| **M3** | Core backend (curriculum + auth) MVP | Backend Team | 2026‑08‑15 |
| **M4** | Lab orchestration prototype (Docker + K8s) | Infra / DevOps | 2026‑09‑01 |
| **M5** | Frontend UI + authoring editor | Frontend Team | 2026‑09‑30 |
| **M6** | Billing & subscription flow | Payments Engineer | 2026‑10‑15 |
| **M7** | End‑to‑end beta launch (5 pilot enterprises) | PM + Customer Success | 2026‑11‑15 |
| **M8** | Iterate on feedback, achieve MRR $45k | Growth Lead | 2027‑02‑01 |
| **M9** | GA release (public) | All | 2027‑03‑15 |

---  

## 8. Risks & Mitigations  

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Lab environment scaling issues | Service degradation | Medium | Auto‑scale K8s node pool; load‑test to 1k concurrent labs. |
| Content authoring bottleneck | Slow curriculum growth | High | Build reusable lesson templates; enable community contributions (future). |
| Compliance (data residency) for enterprise | Deal loss | Low | Deploy optional EU‑region cluster; document data handling. |
| Stripe integration downtime | Revenue interruption | Low | Implement fallback to manual invoicing for Enterprise tier. |
| Competition releases AI‑driven hints | Feature lag | Medium | Prioritize LLM integration in Phase 2; differentiate with verified labs. |

---  

## 9. Acceptance Criteria (MVP)  

1. A new learner can **sign up**, select a learning path, and complete at least **3 modules** with labs, receiving a badge.  
2. **Lab provisioning** time ≤ 10 seconds; reset ≤ 5 seconds.  
3. **Progress dashboard** accurately reflects completed lessons, quiz scores, and time spent.  
4. **Subscription flow** works for Free, Pro, and Enterprise tiers; access restrictions enforced.  
5. **Analytics** can export a CSV report for a given cohort with ≥ 95 % data accuracy.  
6. System meets **99.5 % uptime** over a 30‑day observation window in staging.  

---  

## 10. Appendices  

* **A. Glossary** – SysAdmin, IaC, Lab Sandbox, Badge, pgvector.  
* **B. Related Repos** – `arkashira/surrogate-1-harvest` (data pipeline), `vllm-project/vllm` (inference engine for future AI hints).  
* **C. Dataset References** – Use `instr-resp` and `messages` datasets for initial lesson content generation and QA pair creation.  

---  

*Prepared by:*  
Senior Product/Engineering Lead – Axentx  
*Approved by:* _______________________   *Date:* _______________________   */
