# CrisisOps IQ Architecture

## High-Level Architecture

```text
                     ┌─────────────────────┐
                     │    Crisis Reports   │
                     └──────────┬──────────┘
                                │

                     ┌─────────────────────┐
                     │    Meeting Notes    │
                     └──────────┬──────────┘
                                │

                     ┌─────────────────────┐
                     │ Operational Signals │
                     └──────────┬──────────┘
                                │

                     ┌─────────────────────┐
                     │ Enterprise Policies │
                     └──────────┬──────────┘
                                │
                                ▼

                  ┌───────────────────────────┐
                  │       Intake Agent        │
                  │ Extract facts & context   │
                  └─────────────┬─────────────┘
                                │
                                ▼

             ┌───────────────────────────────────┐
             │   Crisis Classifier Agent         │
             │ Type, Severity, Impact Assessment │
             └─────────────┬─────────────────────┘
                           │
                           ▼

             ┌───────────────────────────────────┐
             │ Knowledge Retrieval Agent         │
             │ Foundry IQ Knowledge Layer        │
             │ Policies • Rules • Templates      │
             └─────────────┬─────────────────────┘
                           │
                           ▼

             ┌───────────────────────────────────┐
             │ Operations Planner Agent          │
             │ Response Plan & Prioritization    │
             └─────────────┬─────────────────────┘
                           │
                           ▼

             ┌───────────────────────────────────┐
             │ Legal & Compliance Agent          │
             │ Governance & Risk Assessment      │
             └─────────────┬─────────────────────┘
                           │
                           ▼

             ┌───────────────────────────────────┐
             │ Communications Agent             │
             │ Stakeholder Communications        │
             └─────────────┬─────────────────────┘
                           │
                           ▼

             ┌───────────────────────────────────┐
             │ Verifier & Safety Agent           │
             │ Human Approval & Safety Checks    │
             └─────────────┬─────────────────────┘
                           │
                           ▼

          ┌─────────────────────────────────────────┐
          │         Executive Dashboard             │
          ├─────────────────────────────────────────┤
          │ Crisis Summary                          │
          │ Severity Score                          │
          │ Root Cause Analysis                     │
          │ Priority Ranking                        │
          │ 24-Hour Action Plan                     │
          │ Resource Allocation                     │
          │ Compliance Review                       │
          │ Stakeholder Communications              │
          │ Human Approval Gates                    │
          │ Audit Log                               │
          └─────────────────────────────────────────┘
```

---

## Microsoft IQ Integration

### Foundry IQ

Foundry IQ acts as the governed enterprise knowledge layer.

It provides:

* Crisis policies
* Escalation rules
* Communication templates
* Governance guidance
* Operational playbooks

The Knowledge Retrieval Agent uses this layer to generate grounded recommendations.

---

## Human-in-the-Loop Governance

Sensitive actions are routed through Human Approval Gates before execution.

Examples:

* Public announcements
* Regulatory notifications
* Customer compensation
* Service shutdown decisions
* Legal admissions

---

## Auditability

Every recommendation includes:

* Reasoning
* Policy reference
* Risk level
* Approval requirement
* Timestamp

to ensure traceability and governance.
