# CrisisOps IQ — Human-in-the-Loop Approval Flow

## Purpose

This document defines the human approval workflow for CrisisOps IQ. It is designed for Microsoft Copilot Studio, Dataverse, Power Automate, Adaptive Cards, and enterprise governance demonstrations.

## Workflow Overview

```text
Incident Detected
→ Classification
→ Severity Assessment
→ Recommendation Generation
→ Human Approval Decision
→ Approved / Rejected / Escalated
→ Audit Log
```

## Step 1: Incident Detected

The Intake Agent retrieves or receives a crisis report from the Incident table.

Required data:

- IncidentID
- IncidentType
- Severity
- Status
- Region
- AssignedTeam
- ImpactedServices
- AffectedUsers
- BusinessImpact

For the demo:

```text
CASE-1001 — Payment Platform Outage
Severity: Critical
Affected Users: 12000
Business Impact: High Revenue Impact
```

## Step 2: Classification

The Crisis Classifier Agent reviews:

- Incident table
- EscalationRule table
- Crisis policy knowledge source

Classification output:

```text
Incident Type: Service Outage
Severity: Critical
Escalation Required: Yes
Compliance Review Required: Yes
Approval Level: Level 3
```

## Step 3: Severity Assessment

Severity is calculated using business impact, affected users, service criticality, and escalation thresholds.

Suggested severity logic:

| Condition | Severity |
|---|---|
| Limited user impact and no external exposure | Low |
| Operational impact with manageable workaround | Medium |
| High user impact, customer-facing disruption, or vendor breach | High |
| Major outage, revenue impact, security risk, or regulatory exposure | Critical |

## Step 4: Recommendation Generation

The Operations Planner Agent generates:

- 24-hour response plan.
- Resource allocation.
- Immediate mitigation.
- Stakeholder communication plan.

The Compliance Agent reviews:

- External communication risk.
- Regulatory notification risk.
- Liability-sensitive language.
- Approval requirements.

The Safety & Verifier Agent checks:

- No sensitive data.
- No unauthorized decision.
- No unsupported claims.
- Human approval requirement included.

## Step 5: Human Approval Decision

Approval is required when:

- Severity is High or Critical.
- Communication is external.
- Compliance, privacy, cybersecurity, or regulatory exposure exists.
- Customer compensation is proposed.
- Vendor enforcement is proposed.
- Public statement is proposed.

## Approval Levels

| Approval Level | Approver Role | Typical Use |
|---|---|---|
| Level 1 | Team Lead | Medium internal operational response |
| Level 2 | Operations Manager | High operational response |
| Level 3 | Executive Sponsor | Critical incident, customer impact, revenue impact |
| Level 4 | Legal / Compliance Lead | Regulatory, privacy, cybersecurity, liability-sensitive action |

## Approval Conditions

| Condition | Required Approval |
|---|---|
| Critical service outage | Level 3 |
| External customer notification | Level 3 |
| Regulatory notification | Level 4 |
| Cybersecurity incident | Level 4 |
| Contractual vendor action | Level 4 |
| Customer compensation | Level 3 + Level 4 |
| Internal-only update for Medium incident | Level 1 or Level 2 |

## Escalation Logic

Escalate when:

1. Approval is pending for more than the defined SLA.
2. The approver rejects but the risk remains unresolved.
3. New evidence increases severity.
4. Compliance review is required but no compliance owner is assigned.
5. External communication is urgent but not yet approved.

Recommended SLA:

| Severity | Approval SLA |
|---|---|
| Low | 8 business hours |
| Medium | 4 business hours |
| High | 1 business hour |
| Critical | 15 minutes |

## Adaptive Card Design

Use this card for approval requests in Microsoft Teams or Copilot Studio.

```json
{
  "type": "AdaptiveCard",
  "version": "1.5",
  "body": [
    {
      "type": "TextBlock",
      "text": "CrisisOps IQ Approval Request",
      "weight": "Bolder",
      "size": "Large"
    },
    {
      "type": "FactSet",
      "facts": [
        {
          "title": "Incident ID",
          "value": "CASE-1001"
        },
        {
          "title": "Title",
          "value": "Payment Platform Outage"
        },
        {
          "title": "Severity",
          "value": "Critical"
        },
        {
          "title": "Requested Action",
          "value": "Approve customer notification and executive war room activation"
        },
        {
          "title": "Approval Level",
          "value": "Level 3 - Executive Approval"
        },
        {
          "title": "Compliance Review",
          "value": "Required before external release"
        }
      ]
    },
    {
      "type": "Input.Text",
      "id": "decisionNote",
      "placeholder": "Add approval, rejection, or escalation note",
      "isMultiline": true
    }
  ],
  "actions": [
    {
      "type": "Action.Submit",
      "title": "Approve",
      "data": {
        "decision": "Approved",
        "incidentId": "CASE-1001"
      }
    },
    {
      "type": "Action.Submit",
      "title": "Reject",
      "data": {
        "decision": "Rejected",
        "incidentId": "CASE-1001"
      }
    },
    {
      "type": "Action.Submit",
      "title": "Escalate",
      "data": {
        "decision": "Escalated",
        "incidentId": "CASE-1001"
      }
    }
  ]
}
```

## Governance Controls

1. All High and Critical recommendations must be logged.
2. External communications cannot be marked as sent unless approval is Approved.
3. Compliance-sensitive actions require Level 4 review.
4. The agent must not bypass rejected approval decisions.
5. Rejected actions must generate an audit log entry.
6. Escalated actions must be routed to the next approval level.
7. Every approval decision must update the Approval table and AuditLog table.
8. The agent must distinguish between draft, approved, and sent communications.

## Recommended Power Automate Flow

```text
Trigger: New Approval record created in Dataverse
Condition: Status = Pending
Action: Post Adaptive Card to Teams approver
Wait for response
Condition:
  - If Approved → update Approval.Status = Approved
  - If Rejected → update Approval.Status = Rejected
  - If Escalated → update Approval.Status = Escalated and assign next approval level
Action: Create AuditLog record
Action: Notify CrisisOps Orchestrator
```

## Demo Approval Scenario

For CASE-1001:

```text
Requested Action:
Approve customer notification and executive war room activation.

Reason:
Payment Gateway outage affects 12000 users and creates high revenue impact.

Required Approval:
Level 3 Executive Approval and compliance review before external release.

Expected Decision:
Approved for executive war room activation.
Customer notification remains pending compliance review.
```
