# CrisisOps IQ Architecture

```text
                    ┌─────────────────────┐
                    │       USER          │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌───────────────────────────┐
                 │   CrisisOps Orchestrator  │
                 │      Copilot Studio       │
                 └──────────┬────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼

┌────────────────┐  ┌────────────────┐  ┌────────────────┐
│ SharePoint     │  │ Dataverse      │  │ Microsoft 365  │
│ Knowledge Base │  │ Operational    │  │ Context        │
│ (Foundry IQ)   │  │ Records        │  │ (Work IQ)      │
└───────┬────────┘  └───────┬────────┘  └───────┬────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ▼

              ┌───────────────────────────┐
              │   Crisis Classification   │
              │ Severity & Impact Analysis│
              └──────────┬────────────────┘
                         ▼

              ┌───────────────────────────┐
              │     Response Planning     │
              │ Priorities & Resources    │
              └──────────┬────────────────┘
                         ▼

              ┌───────────────────────────┐
              │ Human Approval Workflow   │
              │ Governance Controls       │
              └──────────┬────────────────┘
                         ▼

              ┌───────────────────────────┐
              │ Governance Audit Workflow │
              │ Decision Traceability     │
              └──────────┬────────────────┘
                         ▼

              ┌───────────────────────────┐
              │ SharePoint Audit Log      │
              │ Audit Repository          │
              └──────────┬────────────────┘
                         ▼

        ┌────────────────┴────────────────┐
        │                                 │
        ▼                                 ▼

┌────────────────┐             ┌────────────────┐
│ Microsoft Teams│             │ Email & M365   │
│ Notifications  │             │ Communications │
└────────────────┘             └────────────────┘
```

## Microsoft IQ Mapping

| Layer | Usage |
|---------|---------|
| Foundry IQ | Crisis policies, playbooks, governance rules |
| Work IQ | Microsoft 365 context, Teams, Mail, Word |
| Fabric IQ Ready | Operational records and analytics expansion |

## Governance Features

- Human Approval Gates
- Compliance Workflow
- Audit Logging
- SharePoint Audit Repository
- Executive Brief Generation
- Enterprise Communications
