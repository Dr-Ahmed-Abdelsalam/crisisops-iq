# CrisisOps IQ — 3–5 Minute Demo Video Script

## Demo Scenario

```text
CASE-1001 — Payment Platform Outage
Incident Type: Service Outage
Severity: Critical
Affected Users: 12000
Business Impact: High Revenue Impact
Assigned Team: TEAM-A
```

## Demo Goal

Show that CrisisOps IQ is not a chatbot. It is an enterprise multi-agent war room solution that uses Copilot Studio concepts, Dataverse grounding, Microsoft IQ concepts, human approval, and audit logging.

## Target Duration

3–5 minutes.

## Demo Structure

| Segment | Duration |
|---|---|
| Opening and problem | 30 seconds |
| Crisis analysis | 45 seconds |
| Multi-agent orchestration | 60 seconds |
| Approval workflow | 60 seconds |
| Communications and audit log | 60 seconds |
| Closing | 30 seconds |

---

## Segment 1 — Opening

### What appears on screen

- GitHub repository or landing page.
- Project title: CrisisOps IQ.
- Tagline: Autonomous Enterprise Multi-Agent War Room Solution.
- Quick view of architecture diagram.

### Presenter says

“CrisisOps IQ is an enterprise war room agent for operational crisis management. It transforms scattered incident reports, operational data, meeting notes, and internal policies into a governed response plan with approvals, stakeholder communications, and audit logging. The demo uses synthetic data only.”

### Agent does

No action yet. Presenter introduces the system.

### Expected output

The viewer understands the product, enterprise use case, and safety posture.

---

## Segment 2 — Crisis Detection

### What appears on screen

- Copilot Studio test chat.
- Prompt typed by presenter:

```text
Analyze CASE-1001 and generate a governed response plan with approval requirements, stakeholder communications, and audit summary.
```

### Presenter says

“I will start with CASE-1001, a payment platform outage. The agent will ground its answer in Dataverse tables and policy knowledge.”

### Agent does

The CrisisOps Orchestrator retrieves:

- Incident record from Incident table.
- Resources from Resource table.
- Escalation rules from EscalationRule table.
- Approval records from Approval table.
- Communication templates from knowledge source.
- Meeting notes for CASE-1001.

### Expected output

```text
Incident ID: CASE-1001
Crisis Summary: Payment Gateway outage affecting 12000 users with high revenue impact.
Severity: Critical
Likely Root Cause: Platform or payment infrastructure failure requiring TEAM-A investigation.
Business Impact: Revenue interruption, customer experience impact, escalation risk.
Human Approval Required: Yes, Level 3 Executive Approval and compliance review before external communication.
```

---

## Segment 3 — Multi-Agent Orchestration

### What appears on screen

- Agent response showing sections:
  - Intake Agent
  - Crisis Classifier Agent
  - Operations Planner Agent
  - Compliance Agent
  - Communications Agent
  - Safety & Verifier Agent

### Presenter says

“The orchestrator coordinates specialized agents. Each agent contributes a controlled part of the final response instead of producing an ungoverned answer.”

### Agent does

- Intake Agent extracts facts.
- Crisis Classifier Agent confirms severity.
- Operations Planner Agent creates a 24-hour action plan.
- Compliance Agent marks external communication as approval-required.
- Communications Agent drafts stakeholder messages.
- Safety & Verifier Agent checks governance rules and audit requirements.

### Expected output

```text
24-Hour Action Plan:
1. Activate incident war room and assign TEAM-A as primary responder.
2. Confirm payment gateway failure scope and affected transaction paths.
3. Prepare customer notification draft, but do not release before approval.
4. Provide executive update within 30 minutes.
5. Review compliance exposure before external communication.
6. Log all recommendations and approval decisions.
```

---

## Segment 4 — Dataverse Grounding

### What appears on screen

- Dataverse table mapping or GitHub `demo_data` folder.
- Tables visible:
  - incidents.csv
  - resources.csv
  - escalation_rules.csv
  - approvals.csv
  - communications.csv
  - audit_log.csv

### Presenter says

“The agent is grounded in structured enterprise data. The Incident table is the central record, while approvals, communications, and audit logs connect back to the same incident ID.”

### Agent does

References source data in the answer.

### Expected output

```text
Source Data Used:
- Incident: CASE-1001
- Resource: TEAM-A
- Escalation Rule: Critical Service Outage
- Approval: Pending Level 3 approval
- Communication Template: Customer Notice
- AuditLog: Recommendation pending approval
```

---

## Segment 5 — Human Approval Workflow

### What appears on screen

- Adaptive Card approval request.
- Buttons:
  - Approve
  - Reject
  - Escalate

### Presenter says

“For Critical incidents, the agent cannot release external communications or execute sensitive actions by itself. It creates a human approval request.”

### Agent does

Creates approval request:

```text
Approval Request:
Incident ID: CASE-1001
Requested Action: Approve customer notification and executive war room activation.
Risk Level: Critical
Approval Level: Level 3
Decision Options: Approve, Reject, Escalate
```

### Expected output

```text
Approval Required:
External customer notification requires Level 3 Executive Approval.
Compliance review is required before external release.
No external communication will be marked as sent until approval is recorded.
```

---

## Segment 6 — Executive Communication

### What appears on screen

- Agent generates executive brief.

### Presenter says

“Once the approval requirement is clear, the Communications Agent drafts a controlled executive brief.”

### Agent does

Generates draft communication.

### Expected output

```text
Executive Brief:
CASE-1001 is a Critical payment platform outage affecting the Payment Gateway in DISTRICT-01. Current estimated impact is 12000 affected users and high revenue impact. TEAM-A has been assigned to immediate stabilization. Customer communication is prepared as a draft and requires executive and compliance approval before release.
```

---

## Segment 7 — Audit Logging

### What appears on screen

- Audit summary in agent response or `audit_log.csv`.

### Presenter says

“Every major recommendation is traceable. This is important for enterprise reliability, accountability, and Responsible AI.”

### Agent does

Creates or displays audit summary.

### Expected output

```text
Audit Summary:
Recommendation: Activate Critical incident response and prepare customer notification.
Reason: Payment outage affects 12000 users and creates high revenue impact.
Source Data: Incident, EscalationRule, Resource, Approval, Communication Template.
Agent Responsible: CrisisOps Orchestrator.
Approval Requirement: Level 3 Executive Approval and compliance review.
Final Outcome: Pending approval.
```

---

## Segment 8 — Closing

### What appears on screen

- Landing page or architecture diagram.
- Final dashboard or GitHub repository.

### Presenter says

“CrisisOps IQ demonstrates an enterprise-grade agent pattern: grounded data, multi-agent reasoning, human approval, safe communications, and audit logging. It is designed for the Enterprise Agents Track and shows how Microsoft Copilot Studio, Dataverse grounding, and Microsoft IQ concepts can support real operational crisis management.”

### Agent does

No further action.

### Expected output

The demo ends with a clear enterprise value proposition.

---

# Recommended Test Prompts

## Prompt 1

```text
Analyze CASE-1001.
```

Expected response:

```text
CASE-1001 is a Critical Payment Platform Outage affecting the Payment Gateway and approximately 12000 users. TEAM-A is assigned. The incident requires Level 3 executive approval before customer notification.
```

## Prompt 2

```text
Generate a 24-hour action plan for CASE-1001.
```

Expected response:

```text
The plan should include war room activation, payment gateway diagnostics, customer impact monitoring, executive update, compliance review, and approval-gated customer communication.
```

## Prompt 3

```text
Draft a customer notification for CASE-1001.
```

Expected response:

```text
The agent drafts a customer notice but clearly marks it as Pending Approval and not ready for external release until Level 3 and compliance approval are complete.
```

## Prompt 4

```text
Show the audit log for CASE-1001.
```

Expected response:

```text
The agent displays recommendation, reason, source data, responsible agent, approval requirement, and final outcome.
```

## Prompt 5

```text
Request approval for CASE-1001 customer communication.
```

Expected response:

```text
The agent creates an approval request with Approve, Reject, and Escalate options and explains why Level 3 approval is required.
```

---

# Judging Criteria Alignment

| Judging Area | How the Demo Shows It |
|---|---|
| Best Enterprise Agent | Real enterprise crisis workflow, not generic chat |
| Best Use of Microsoft IQ Concepts | Foundry IQ policy grounding, Work IQ meeting notes simulation, Dataverse structured grounding |
| Reasoning & Multi-Step Thinking | Intake → classify → plan → compliance → communication → approval → audit |
| Reliability & Safety | Human approval gates and compliance checks |
| User Experience | Clear prompts, dashboard-ready data, short executive output |
| Community Vote | Simple visual story: crisis enters, governed response exits |
