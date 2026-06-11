# CrisisOps IQ — Dataverse Schema

## Purpose

This document defines the Dataverse model for CrisisOps IQ based on the synthetic `demo_data` package. The model is designed for Copilot Studio grounding, multi-agent orchestration, human approval workflows, dashboard visualization, and audit logging.

## Table 1: Incident

### Purpose

Stores the primary crisis record. This is the central table used by the Intake Agent, Crisis Classifier Agent, Operations Planner Agent, Compliance Agent, and CrisisOps Orchestrator.

### Primary Key

`IncidentID`

### Columns

| Column | Type | Description |
|---|---|---|
| IncidentID | Text | Unique synthetic incident identifier, e.g., CASE-1001 |
| Title | Text | Short incident title |
| IncidentType | Choice | Service Outage, Supply Chain Disruption, Customer Complaint Surge, Compliance Incident, Cybersecurity Alert, Project Delay, Resource Shortage, Vendor Failure |
| Severity | Choice | Low, Medium, High, Critical |
| Status | Choice | Open, Investigating, Mitigating, Escalated, Resolved |
| Region | Text | Synthetic region, e.g., DISTRICT-01 |
| ReportedBy | Text | Synthetic employee ID |
| AssignedTeam | Text | Synthetic team ID |
| CreatedDate | DateTime | Incident creation timestamp |
| LastUpdated | DateTime | Last update timestamp |
| ImpactedServices | Text | Affected business service |
| AffectedUsers | Number | Estimated affected users |
| BusinessImpact | Text | Business impact description |

### Relationships

- Incident 1:N Approval
- Incident 1:N Communication
- Incident 1:N AuditLog
- Incident 1:N Feedback
- Incident N:1 Resource through `AssignedTeam`
- Incident N:1 EscalationRule through `IncidentType` and `Severity`

### Example Record

```text
IncidentID: CASE-1001
Title: Payment Platform Outage
IncidentType: Service Outage
Severity: Critical
Status: Open
Region: DISTRICT-01
AssignedTeam: TEAM-A
ImpactedServices: Payment Gateway
AffectedUsers: 12000
BusinessImpact: High Revenue Impact
```

---

## Table 2: Resource

### Purpose

Stores operational teams, capacity, availability, and skills used by the Operations Planner Agent.

### Primary Key

`ResourceID`

### Columns

| Column | Type | Description |
|---|---|---|
| ResourceID | Text | Unique resource identifier |
| TeamID | Text | Synthetic team ID |
| TeamName | Text | Functional team name |
| Capability | Text | Core capability |
| Availability | Choice | Available, Limited, Unavailable |
| Capacity | Number | Available capacity percentage or units |
| Region | Text | Synthetic operating region |
| Owner | Text | Synthetic employee ID |
| EscalationContact | Text | Synthetic escalation owner |

### Relationships

- Resource 1:N Incident through `TeamID`
- Resource 1:N AuditLog through team assignment references

### Example Record

```text
ResourceID: RES-001
TeamID: TEAM-A
TeamName: Platform Reliability Team
Capability: Payment infrastructure recovery
Availability: Available
Capacity: 80
Region: DISTRICT-01
Owner: EMP-021
```

---

## Table 3: Approval

### Purpose

Stores human approval requests and decisions. This table is essential for governance and Responsible AI controls.

### Primary Key

`ApprovalID`

### Columns

| Column | Type | Description |
|---|---|---|
| ApprovalID | Text | Unique approval identifier |
| IncidentID | Lookup | Related Incident |
| RequestedBy | Text | Synthetic requester |
| Approver | Text | Synthetic approver |
| ApprovalLevel | Choice | Level 1, Level 2, Level 3, Level 4 |
| Status | Choice | Pending, Approved, Rejected, Escalated |
| RequestedAction | Text | Action requiring approval |
| Timestamp | DateTime | Approval request timestamp |
| DecisionNote | Text | Approval or rejection reason |

### Relationships

- Approval N:1 Incident
- Approval 1:N AuditLog when approval decision affects outcome

### Example Record

```text
ApprovalID: APR-1001
IncidentID: CASE-1001
RequestedBy: EMP-001
Approver: EMP-090
ApprovalLevel: Level 3
Status: Pending
RequestedAction: Send external customer notification
```

---

## Table 4: Communication

### Purpose

Stores generated or sent stakeholder communications.

### Primary Key

`CommunicationID`

### Columns

| Column | Type | Description |
|---|---|---|
| CommunicationID | Text | Unique communication identifier |
| IncidentID | Lookup | Related Incident |
| CommunicationType | Choice | Executive Brief, Customer Notification, Internal Update, Regulatory Notification |
| Audience | Text | Target stakeholder group |
| DraftMessage | Multiline Text | Draft or final communication |
| Status | Choice | Draft, Pending Approval, Approved, Sent, Rejected |
| RequiresApproval | Boolean | Whether human approval is required |
| CreatedByAgent | Text | Responsible agent |
| Timestamp | DateTime | Creation timestamp |

### Relationships

- Communication N:1 Incident
- Communication N:1 Approval if external or sensitive

### Example Record

```text
CommunicationID: COM-1001
IncidentID: CASE-1001
CommunicationType: Executive Brief
Audience: Executive Leadership
Status: Pending Approval
RequiresApproval: Yes
CreatedByAgent: Communications Agent
```

---

## Table 5: AuditLog

### Purpose

Stores traceable reasoning and governance records for agent recommendations.

### Primary Key

`AuditID`

### Columns

| Column | Type | Description |
|---|---|---|
| AuditID | Text | Unique audit log identifier |
| IncidentID | Lookup | Related Incident |
| Recommendation | Text | Agent recommendation |
| Reason | Multiline Text | Reasoning behind recommendation |
| SourceData | Text | Tables or files used |
| AgentResponsible | Choice | Intake Agent, Crisis Classifier Agent, Operations Planner Agent, Compliance Agent, Communications Agent, Safety & Verifier Agent, CrisisOps Orchestrator |
| ApprovalRequirement | Text | Required approval gate |
| FinalOutcome | Text | Approved, Rejected, Escalated, Pending, Logged |

### Relationships

- AuditLog N:1 Incident
- AuditLog may reference Approval and Communication by ID in SourceData

### Example Record

```text
AuditID: AUD-1001
IncidentID: CASE-1001
Recommendation: Trigger Critical incident response and executive approval.
Reason: Payment gateway outage affects 12000 users with high revenue impact.
SourceData: Incident, EscalationRule, Resource, Approval
AgentResponsible: CrisisOps Orchestrator
ApprovalRequirement: Level 3 Executive Approval
FinalOutcome: Pending
```

---

## Table 6: EscalationRule

### Purpose

Stores severity thresholds and escalation logic used by the Crisis Classifier Agent and Safety & Verifier Agent.

### Primary Key

`RuleID`

### Columns

| Column | Type | Description |
|---|---|---|
| RuleID | Text | Unique rule identifier |
| IncidentType | Choice | Incident category |
| Severity | Choice | Low, Medium, High, Critical |
| TriggerCondition | Text | Rule condition |
| RequiredAction | Text | Required escalation or response |
| ApprovalLevel | Choice | Level 1, Level 2, Level 3, Level 4 |
| CommunicationRequired | Boolean | Whether stakeholder communication is required |
| ComplianceReviewRequired | Boolean | Whether legal/compliance review is required |

### Relationships

- EscalationRule 1:N Incident by `IncidentType` and `Severity`
- EscalationRule 1:N Approval by `ApprovalLevel`

### Example Record

```text
RuleID: RULE-001
IncidentType: Service Outage
Severity: Critical
TriggerCondition: Affected users exceed 10000 or high revenue impact
RequiredAction: Activate executive war room and customer communication review
ApprovalLevel: Level 3
CommunicationRequired: Yes
ComplianceReviewRequired: Yes
```

---

## Table 7: Feedback

### Purpose

Stores post-incident feedback used for continuous improvement and demo analytics.

### Primary Key

`FeedbackID`

### Columns

| Column | Type | Description |
|---|---|---|
| FeedbackID | Text | Unique feedback identifier |
| IncidentID | Lookup | Related Incident |
| SubmittedBy | Text | Synthetic employee or stakeholder ID |
| Rating | Number | 1–5 score |
| FeedbackType | Choice | Process, Communication, Response Time, Compliance, Resource Allocation |
| Comment | Multiline Text | Feedback summary |
| Timestamp | DateTime | Feedback timestamp |

### Relationships

- Feedback N:1 Incident
- Feedback may inform future escalation rules and response planning

### Example Record

```text
FeedbackID: FB-1001
IncidentID: CASE-1001
SubmittedBy: EMP-050
Rating: 4
FeedbackType: Response Time
Comment: Initial classification was fast; customer communication needed approval earlier.
```

---

## Entity Relationship Diagram

```text
Incident
  ├── 1:N Approval
  ├── 1:N Communication
  ├── 1:N AuditLog
  ├── 1:N Feedback
  ├── N:1 Resource via AssignedTeam = TeamID
  └── N:1 EscalationRule via IncidentType + Severity

Resource
  └── 1:N Incident

EscalationRule
  └── 1:N Incident

Approval
  ├── N:1 Incident
  └── 1:N AuditLog references

Communication
  ├── N:1 Incident
  └── N:1 Approval when approval is required

AuditLog
  └── N:1 Incident

Feedback
  └── N:1 Incident
```

## Dataverse Grounding Strategy

1. Use `Incident` as the central grounding table.
2. Connect `Approval`, `Communication`, `AuditLog`, and `Feedback` to `Incident` through `IncidentID`.
3. Use `Resource` to support operational planning and team allocation.
4. Use `EscalationRule` to support severity classification and approval routing.
5. Add `crisis_policy.md` and `communication_templates.md` as knowledge sources in Copilot Studio.
6. Use `meeting_notes.txt` as Work IQ simulation for CASE-1001.
7. For demo reliability, pin CASE-1001 as the primary scenario and validate that related records exist across all tables.
8. In Copilot Studio, configure topics to retrieve incident details first, then related tables.
9. Use audit records to explain why the agent recommended a given action.
10. Use approval records to demonstrate human-in-the-loop governance.
