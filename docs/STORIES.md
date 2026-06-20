# STORIES.md
**Project:** admin-bootcamp  
**Product Type:** Structured learning platform for system administration (beginner‑friendly)  
**Target Release:** MVP → v1.0  

---  

## Table of Contents
1. [Epics Overview](#epics-overview)  
2. [User Story Backlog](#user-story-backlog)  
   - [Epic 1 – Core Learning Experience](#epic-1--core-learning-experience)  
   - [Epic 2 – Progress Tracking & Gamification](#epic-2--progress-tracking--gamification)  
   - [Epic 3 – Content Management & Authoring](#epic-3--content-management--authoring)  
   - [Epic 4 – Community & Support](#epic-4--community--support)  
3. [Prioritisation for MVP](#prioritisation-for-mvp)  

---  

## Epics Overview
| Epic ID | Title | Goal | MVP Inclusion |
|---------|-------|------|---------------|
| **E1** | Core Learning Experience | Deliver a clean, guided path through foundational system‑admin topics. | ✅ |
| **E2** | Progress Tracking & Gamification | Motivate learners by visualising progress, awarding badges, and enabling self‑assessment. | ✅ |
| **E3** | Content Management & Authoring | Allow product team to create, version, and schedule new modules without code changes. | ✅ |
| **E4** | Community & Support | Provide peer‑to‑peer help, Q&A, and instructor assistance to reduce churn. | ❌ (post‑MVP) |

---  

## User Story Backlog  

### Epic 1 – Core Learning Experience
| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E1‑US1** | **As a new learner, I want a welcome tour, so that I understand how to navigate the platform.** | 1. Tour appears on first login.<br>2. Covers dashboard, module list, and progress bar.<br>3. User can skip or replay the tour. |
| **E1‑US2** | **As a learner, I want a curated learning path (e.g., “Linux Basics → Networking → Security”), so that I can follow a logical progression.** | 1. Path is displayed as a vertical stepper.<br>2. Each step shows module title, estimated time, and prerequisites.<br>3. Learner can mark a step as “Completed”. |
| **E1‑US3** | **As a learner, I want each module to contain short video, interactive terminal sandbox, and a knowledge check, so that I can apply concepts immediately.** | 1. Video player loads within module page.<br>2. Embedded sandbox provides a real‑time Linux shell (Docker‑based).<br>3. Knowledge check consists of 3‑5 multiple‑choice questions; passing score ≥80 %. |
| **E1‑US4** | **As a learner, I want to bookmark a module, so that I can resume it later.** | 1. “Bookmark” button toggles state.<br>2. Bookmarked items appear in a “Saved for later” section on the dashboard.<br>3. State persists across sessions. |
| **E1‑US5** | **As a learner, I want to search for topics, so that I can quickly find relevant modules.** | 1. Search bar supports keyword and tag filtering.<br>2. Results show module title, short description, and relevance score.<br>3. Clicking a result navigates to the module. |
| **E1‑US6** | **As an admin, I want to upload new video assets and sandbox Docker images, so that content stays up‑to‑date.** | 1. Admin UI provides file upload (max 500 MB) with progress bar.<br>2. Uploaded assets are stored in the CDN and referenced in module metadata.<br>3. New assets become available after a single “Publish” click. |

### Epic 2 – Progress Tracking & Gamification
| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E2‑US1** | **As a learner, I want a personal dashboard showing my overall progress, so that I can see how far I’ve come.** | 1. Dashboard displays % of completed modules, total hours learned, and upcoming modules.<br>2. Progress bar updates in real time after each completed knowledge check. |
| **E2‑US2** | **As a learner, I want to earn badges for milestones (e.g., “First Module Completed”, “Linux Shell Pro”), so that I stay motivated.** | 1. Badges are awarded automatically when criteria are met.<br>2. Badge list is visible on the profile page with description and date earned.<br>3. Badge icons appear next to the learner’s name in community posts. |
| **E2‑US3** | **As a learner, I want a “Streak” counter, so that I am encouraged to study daily.** | 1. Counter increments when a learner completes any activity on consecutive days.<br>2. Streak resets to zero after a missed day.<br>3. Visual cue (fire icon) appears when streak ≥7 days. |
| **E2‑US4** | **As a learner, I want to export my learning report (PDF/CSV), so that I can share it with employers or mentors.** | 1. Export button generates a PDF with module list, scores, and badges.<br>2. CSV includes timestamps, module IDs, and pass/fail status.<br>3. Export respects user privacy settings. |
| **E2‑US5** | **As an admin, I want analytics on module completion rates, so that I can identify gaps in the curriculum.** | 1. Admin dashboard shows per‑module completion %, average score, and drop‑off points.<br>2. Data can be filtered by date range and learner cohort.<br>3. Exportable as CSV. |

### Epic 3 – Content Management & Authoring
| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E3‑US1** | **As a content author, I want a markdown‑based authoring UI, so that I can write and preview module content quickly.** | 1. Editor supports live markdown preview.<br>2. Author can add metadata: title, tags, estimated time, prerequisites.<br>3. Drafts are saved automatically every 30 seconds. |
| **E3‑US2** | **As a content author, I want version control for modules, so that I can roll back changes if needed.** | 1. Each save creates a version entry with timestamp and author ID.<br>2. UI shows version history with diff view.<br>3. “Revert to this version” button restores selected version. |
| **E3‑US3** | **As a content author, I want to schedule module publication, so that releases align with marketing campaigns.** | 1. Publish date picker allows future dates.<br>2. Scheduled modules are hidden from learners until the date passes.<br>3. Admin receives email reminder 24 h before go‑live. |
| **E3‑US4** | **As a content author, I want to tag modules with competency levels (Beginner, Intermediate, Advanced), so that learners can filter by skill.** | 1. Tag selector includes predefined levels and custom tags.<br>2. Tags appear on module cards and are searchable. |
| **E3‑US5** | **As a system integrator, I want an API endpoint to fetch published modules in JSON, so that external tools can surface content.** | 1. `GET /api/v1/modules?status=published` returns list with id, title, slug, tags, and asset URLs.<br>2. Supports pagination and ETag caching. |

### Epic 4 – Community & Support (Post‑MVP)
| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E4‑US1** | **As a learner, I want a discussion thread per module, so that I can ask questions and see answers.** | 1. Thread appears at bottom of module page.<br>2. Authenticated users can post, edit, and delete their comments.<br>3. Moderation tools for admins (flag, hide). |
| **E4‑US2** | **As a learner, I want to schedule live office‑hours with an instructor, so that I can get real‑time help.** | 1. Calendar widget shows upcoming slots.<br>2. Learner can book a 30‑min slot; confirmation email sent.<br>3. Instructor joins via integrated video link. |
| **E4‑US3** | **As an admin, I want to define “Frequently Asked Questions” per module, so that common issues are answered instantly.** | 1. FAQ editor allows Q&A pairs with markdown.<br>2. FAQ section is collapsible on module page.<br>3. Search includes FAQ content. |

---  

## Prioritisation for MVP
1. **Epic 1 – Core Learning Experience** (all stories E1‑US1 to E1‑US6) – foundation of the product.  
2. **Epic 2 – Progress Tracking & Gamification** (E2‑US1 to E2‑US5) – drives engagement and provides measurable outcomes.  
3. **Epic 3 – Content Management & Authoring** (E3‑US1 to E3‑US5) – enables rapid iteration of curriculum without developer involvement.  

*Epic 4* will be scoped for the **v1.1** release after validating user adoption and willingness‑to‑pay.  

---  

*Prepared by:* Senior Product/Engineering Lead – admin‑bootcamp  
*Date:* 2026‑06‑20
