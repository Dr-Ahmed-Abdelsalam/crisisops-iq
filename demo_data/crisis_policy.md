# CrisisOps IQ Synthetic Crisis Management Policy

**Demo data notice:** This demo uses synthetic or redacted data only. Do not upload confidential, personal, privileged, or sensitive information.

## 1. Purpose
This synthetic policy governs how CrisisOps IQ classifies incidents, prioritizes response, routes approvals, drafts communications, and records audit evidence during enterprise crisis simulations.

## 2. Incident Classification Rules
- **Low:** Limited business impact, no SLA risk, no external communication, and fewer than 300 affected synthetic users.
- **Medium:** Moderate operational impact, potential delay, or internal dependency risk.
- **High:** SLA risk, revenue risk above USD 50,000, client-visible impact, or resource shortage affecting response commitments.
- **Critical:** Core service outage, cybersecurity containment event, broad customer impact, or any incident requiring executive oversight.

## 3. Escalation Thresholds
- Escalate to L1 when an incident is Medium or above.
- Escalate to L2 when SLA risk equals Yes, estimated users affected exceed 1,000, or a vendor breach is suspected.
- Escalate to L3 for compliance incidents, regulatory communications, and customer-facing high-severity events.
- Escalate to Executive approval for Critical incidents, public statements, major customer impact, or high-risk remediation.

## 4. Approval Requirements
Human approval is mandatory before:
- Sending external customer or regulatory communications.
- Taking actions that may interrupt customer service.
- Making compliance, privacy, legal, or liability-sensitive determinations.
- Reallocating critical resources away from other active high-severity incidents.

## 5. Communication Rules
- Communications must be factual, time-bound, and limited to verified synthetic data.
- Customer notices must include impact, workaround if available, next update time, and support channel.
- Executive briefs must include severity, impact, recommended action, decision required, and risks.
- Regulatory notifications must be reviewed by the Compliance Agent and approved by an authorized human approver.

## 6. Governance Controls
- Every recommendation must include a source reference and agent responsible.
- The Safety & Verifier Agent must flag unverified assumptions.
- The Orchestrator must preserve an audit log explaining the reason for each recommendation.
- The system is advisory only and must not replace authorized human decision-making.
