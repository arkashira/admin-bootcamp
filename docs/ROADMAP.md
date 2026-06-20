# ROADMAP.md – admin‑bootcamp

## Vision
Create a **structured, beginner‑friendly learning platform** that guides aspiring system administrators through a clear, progressive curriculum, equips them with hands‑on labs, and validates competence with certifications. The platform will be the go‑to entry point for anyone looking to break into sysadmin roles, driving user growth and establishing a recurring revenue stream for Axentx.

---

## Milestones Overview

| Milestone | Target Release | Description | MVP‑Critical? |
|-----------|----------------|-------------|---------------|
| **MVP – Launch Ready** | **2026‑09‑30** | Core learning experience that can be released to early‑adopters and generate validated demand. | **Yes** |
| **v1 – Community & Expansion** | 2027‑03‑31 | Add community features, richer content, and integration with Axentx’s credentialing system. | No |
| **v2 – Enterprise & Automation** | 2027‑10‑31 | Enterprise onboarding, SSO, reporting dashboards, and AI‑driven lab assistance. | No |

---

## 1️⃣ MVP – Launch Ready (Target: 2026‑09‑30)

| Feature | Description | Acceptance Criteria |
|---------|-------------|----------------------|
| **Curriculum Engine** | Structured learning path (Intro → Core → Advanced) with prerequisite enforcement. | Users cannot skip modules; progress bar updates in real time. |
| **Content Library** | 12 beginner modules (Linux basics, networking, users & permissions, shell scripting, monitoring, etc.) with markdown + embedded videos. | Each module contains at least 1 reading, 1 video, and 1 quiz. |
| **Interactive Labs** | Container‑based sandbox (Docker + `vLLM` for AI‑assisted hints) for hands‑on tasks. | Lab spins up in ≤5 s, persists state for the session, and auto‑resets on completion. |
| **Assessment & Certification** | End‑of‑track quiz (20 questions) + practical lab exam; generate PDF certificate on pass. | Pass rate ≥70 % yields downloadable certificate with unique QR code. |
| **User Management (Auth)** | Email/password sign‑up, email verification, password reset. | Secure storage (bcrypt), rate‑limited login, GDPR‑compliant data handling. |
| **Admin Dashboard** | CRUD for modules, labs, quizzes; view user progress & analytics. | Admin can publish/unpublish content without downtime. |
| **Responsive UI** | Mobile‑first design, accessible (WCAG 2.1 AA). | All core flows work on iOS/Android browsers. |
| **Telemetry & Feedback Loop** | Capture completion rates, time‑on‑task, and NPS survey. | Data stored in Axentx BRAIN for downstream validation. |
| **CI/CD Pipeline** | Automated tests, linting, Docker image builds, and staged deployments. | 90 % test coverage on core services; zero‑downtime deploys. |

### MVP Success Metrics
- **≥1,000** registered users within 30 days of launch.  
- **≥30 %** of users complete the full track and earn a certificate.  
- **NPS ≥ 45** from early‑adopter survey.  
- **Validated willingness‑to‑pay** (≥10 % conversion to paid “Pro” tier in pilot).  

---

## 2️⃣ v1 – Community & Expansion (Target: 2027‑03‑31)

| Theme | Key Features |
|-------|--------------|
| **Community & Social Learning** | Discussion forums per module, peer‑reviewed lab submissions, mentorship matching. |
| **Content Growth** | Add 8 intermediate modules (e.g., SELinux, Docker orchestration, log analysis). |
| **Gamification** | Badges, leaderboards, streak tracking to boost engagement. |
| **Pro Tier & Monetization** | Subscription model unlocking advanced labs, offline PDFs, and priority AI‑hint support. |
| **Analytics Dashboard** | Exportable CSV reports, cohort analysis for enterprise partners. |
| **Localization** | UI and core content translated into Spanish, French, Mandarin (initial). |
| **Integration with Axentx Credentialing** | Auto‑sync certificates to Axentx profile, enable badge display on LinkedIn. |

### v1 Success Metrics
- **≥5,000** active users (monthly).  
- **≥15 %** conversion to Pro tier.  
- **Community engagement**: average 3 posts/user/month.  

---

## 3️⃣ v2 – Enterprise & Automation (Target: 2027‑10‑31)

| Theme | Key Features |
|-------|--------------|
| **Enterprise Onboarding** | SSO (SAML/OIDC), role‑based access control, bulk user import. |
| **Advanced Lab Automation** | AI‑driven lab guidance powered by `vLLM` + `SGLang` for step‑by‑step hints and auto‑grading. |
| **Custom Curriculum Builder** | Admins can assemble bespoke learning paths from existing modules or upload proprietary content. |
| **Reporting & Compliance** | Real‑time dashboards, audit logs, GDPR/CCPA data export tools. |
| **API & Integrations** | REST/GraphQL API for LMS integration (e.g., Moodle, Canvas). |
| **Performance & Scalability** | Horizontal scaling of lab containers, load‑balanced front‑end, CDN for media assets. |
| **Enterprise Pricing & Licensing** | Tiered contracts, volume discounts, on‑premise deployment option (Docker‑Compose/K8s). |

### v2 Success Metrics
- **≥10 enterprise contracts** signed within 6 months of release.  
- **≥99.9 %** uptime SLA for lab environments.  
- **AI‑hint adoption**: ≥40 % of lab sessions use AI assistance, with ≥90 % satisfaction rating.  

---

## Release Process & Governance

1. **Sprint Planning** – 2‑week sprints, backlog prioritized by MVP‑critical items first.  
2. **Design Review** – UI/UX mockups approved by PM & Accessibility lead.  
3. **Feature Development** – Feature branches merged via PRs with mandatory code‑review and automated tests.  
4. **Staging Validation** – End‑to‑end smoke tests, security scan, and performance benchmark.  
5. **Beta Launch** – Closed‑beta for internal staff + 200 external users; collect telemetry.  
6. **Go‑Live** – Incremental rollout behind feature flag; monitor key metrics in real time.  
7. **Post‑Launch Review** – Retrospective, update BRAIN with validation data, iterate.

---

## Dependencies & Risks

| Dependency | Owner | Mitigation |
|------------|-------|------------|
| **Container Lab Infrastructure** | DevOps | Use proven `vLLM`‑backed images; maintain fallback to plain Docker. |
| **AI Hint Engine** | ML Team | Start with rule‑based hints; upgrade to `vLLM` + `SGLang` in v2. |
| **Content Creation** | Content Lead | Leverage existing open‑source sysadmin guides; contract SMEs for gaps. |
| **Compliance (GDPR/CCPA)** | Legal | Early audit, privacy‑by‑design, data‑retention policies. |
| **Scalability** | Infrastructure | Auto‑scaling groups, load testing before each major release. |

---

## Appendices

- **Link to Repo:** `github.com/arkashira/admin-bootcamp`  
- **Runbook Location:** `🗺️ AXENTX RUNBOOK + LOCATIONS (2026-05-23)` – see “deployment” section for CI/CD details.  
- **Dataset Utilization:** Leverage `instr-resp` and `messages` datasets to pre‑populate FAQ bots and AI hint models.  

--- 

*Prepared by the Senior Product/Engineering Lead, admin‑bootcamp – Axentx*
