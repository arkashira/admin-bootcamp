# breakeven.md  

**Product:** *admin‑bootcamp* – a structured, beginner‑friendly learning platform for system‑administration.  

---  

## 1. Cost per Active User (monthly)  

| Cost Component | Assumptions (per active user) | Monthly Cost (USD) |
|----------------|------------------------------|--------------------|
| **Compute** (2 vCPU + 4 GB RAM container running the learning UI + background job workers) | 0.05 vCPU‑hour + 0.1 GB‑hour on AWS t3.medium (≈ $0.040/vCPU‑hr, $0.004/GB‑hr) | **$0.006** |
| **Storage** (user profile + progress data ≈ 5 MB, shared course assets cached on CDN) | 5 MB on S3 Standard ($0.023/GB‑mo) + 10 GB CDN cache per 1 k users (shared) | **$0.001** |
| **Bandwidth** (average 2 GB of video/interactive content streamed per user per month) | 2 GB @ $0.09/GB (AWS CloudFront) | **$0.18** |
| **Third‑party services** (email (SendGrid) + auth (Auth0) per user) | 0.5 email / mo @ $0.10/10k + Auth0 free tier (negligible) | **$0.005** |
| **Total variable cost / active user** |  | **≈ $0.192** |

> **Rounded to $0.20 per active user / month** for budgeting (covers a small safety margin for occasional spikes).

### Fixed overhead (monthly)  

| Item | Monthly Cost (USD) |
|------|--------------------|
| Core infra (load balancer, DB primary, monitoring) | $250 |
| DevOps / SRE on‑call (0.2 FTE) | $800 |
| License / tooling (CI/CD, analytics) | $150 |
| **Total Fixed** | **$1,200** |

---

## 2. Pricing Tiers  

| Tier | Monthly Price (USD) | Core Features | Target Persona |
|------|--------------------|----------------|----------------|
| **Starter** | **$9** | • Access to all beginner modules (0‑30 hrs) <br>• Community forum <br>• Progress dashboard | Hobbyists / boot‑camp students |
| **Professional** | **$29** | • Everything in Starter <br>• Intermediate & advanced labs (30‑80 hrs) <br>• Hands‑on labs with live VM sandbox <br>• Certificate of completion | Junior sysadmins, career‑switchers |
| **Enterprise** | **$79** | • All Professional features <br>• Team admin console (user groups, reporting) <br>• Private on‑premise sandbox option <br>• Dedicated support SLA <br>• API access for LMS integration | Small IT training departments, staffing agencies |

*Assume 70 % of paying users choose Professional, 20 % Starter, 10 % Enterprise (typical SaaS distribution).*

---

## 3. Customer Acquisition Cost (CAC)  

| Channel | Cost per Lead | Conversion (lead → paying) | CAC (USD) |
|---------|---------------|----------------------------|-----------|
| Content/SEO (blog, tutorials) | $0.50 | 2 % | **$25** |
| Paid social (LinkedIn, Reddit) | $1.20 | 3 % | **$40** |
| Partnerships / boot‑camp referrals | $0.80 | 5 % | **$16** |
| **Weighted average CAC** (assuming 40 % SEO, 30 % paid, 30 % partners) | — | — | **≈ $27** |

*Range: $16 – $40 per new paying subscriber.*

---

## 4. Lifetime Value (LTV)  

Assumptions  

* Average churn = 5 % per month (typical for niche education SaaS).  
* Average revenue per paying user (ARPU) = weighted price:  

\[
ARPU = 0.2·9 + 0.7·29 + 0.1·79 = 1.8 + 20.3 + 7.9 = **\$30.0**\text{/mo}
\]

* Customer lifetime (months) = 1 / churn = 1 / 0.05 = **20 months**.  

\[
LTV = ARPU × Lifetime = 30 × 20 = **\$600**
\]

**LTV / CAC ratio ≈ 600 / 27 ≈ 22 ×** – well above the healthy >3× benchmark.

---

## 5. Break‑Even Users Count  

Break‑even occurs when **Monthly Revenue ≥ Fixed Costs + Variable Cost × Active Users**.

Let **U** = number of paying active users.

\[
Revenue = ARPU × U
\]
\[
Cost = Fixed + (Variable\;Cost) × U = 1,200 + 0.20U
\]

Set Revenue = Cost:

\[
30U = 1,200 + 0.20U \\
30U - 0.20U = 1,200 \\
29.8U = 1,200 \\
U ≈ 40.3
\]

**≈ 41 paying users** (any tier mix that yields $30 ARPU) are needed to cover all costs.

If we consider the tier mix explicitly:

| Tier mix (40 users) | Monthly Rev | Variable Cost (0.20×U) | Total Cost | Net |
|---------------------|-------------|------------------------|------------|-----|
| 8 Starter ($9) + 28 Professional ($29) + 4 Enterprise ($79) | 8·9 + 28·29 + 4·79 = **$1,240** | $8 | $1,208 | **+$32** |

Thus, **≈ 40 – 45 paying users** is the practical break‑even point.

---

## 6. Path to $10 K MRR  

Goal: $10,000 monthly recurring revenue.

Using the weighted ARPU of $30:

\[
Required\;users = \frac{10,000}{30} ≈ 334\;paying\;users
\]

Break‑down by tier (maintaining the 20/70/10 distribution):

| Tier | Users | Monthly Rev |
|------|-------|-------------|
| Starter (20 %) | 67 | 67 × $9 = $603 |
| Professional (70 %) | 234 | 234 × $29 = $6,786 |
| Enterprise (10 %) | 33 | 33 × $79 = $2,607 |
| **Total** | **334** | **$10, - ≈ $10, -** |

**Alternative “fast‑track”** – push more Enterprise sales:

| Scenario | Enterprise % | Users | Rev |
|----------|--------------|-------|-----|
| Aggressive B2B push | 20 % | 67 Ent, 200 Prof, 67 Start | 67·79 + 200·29 + 67·9 = $5,293 + $5,800 + $603 = **$11,696** |

Thus, **334 paying users** (or ~70 Enterprise‑focused users) will comfortably exceed $10 K MRR.

---

## 7. Summary of Key Numbers  

| Metric | Value |
|--------|-------|
| Variable cost / active user | **$0.20 / mo** |
| Fixed monthly overhead | **$1,200** |
| Break‑even paying users | **≈ 41** |
| CAC (average) | **$27** (range $16‑$40) |
| LTV (average) | **$600** |
| LTV / CAC | **≈ 22×** |
| Users for $10 K MRR | **≈ 334** (≈ 67 Starter, 234 Professional, 33 Enterprise) |
| Time to $10 K MRR (assuming 5 % monthly churn, 10 % conversion from free trial) | ~6‑8 months with a modest acquisition budget of $5‑7 k/mo (≈ 150‑250 new leads) |

These figures provide a concrete financial foundation for the **admin‑bootcamp** launch and guide go‑to‑market budgeting, pricing optimisation, and growth targets.  