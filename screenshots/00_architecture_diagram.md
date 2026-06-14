
  # CrisisOps IQ Enterprise Agent Architecture

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

      ┌─────────────────────┼─────────────────────┐
      ▼                     ▼                     ▼

┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ Foundry IQ    │   │ Dataverse     │   │ Work IQ       │
│ Knowledge     │   │ Operational   │   │ M365 Context  │
│ Policies      │   │ Records       │   │ Mail & Word   │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        └──────────────┬──────────────┘
                       ▼

        ┌──────────────────────────────┐
        │        Intake Agent          │
        │ Incident Fact Extraction     │
        └──────────────┬───────────────┘
                       ▼

        ┌──────────────────────────────┐
        │ Crisis Classifier Agent      │
        │ Severity & Impact Analysis   │
        └──────────────┬───────────────┘
                       ▼

        ┌──────────────────────────────┐
        │ Operations Planner Agent     │
        │ Actions & Resources          │
        └──────────────┬───────────────┘
                       ▼

        ┌──────────────────────────────┐
        │ Compliance Agent             │
        │ Governance & Risk Review     │
        └──────────────┬───────────────┘
                       ▼

        ┌──────────────────────────────┐
        │ Communications Agent         │
        │ Teams / Email Drafting       │
        └──────────────┬───────────────┘
                       ▼

        ┌──────────────────────────────┐
        │ Safety & Verifier Agent      │
        │ Approval Validation          │
        └──────────────┬───────────────┘
                       ▼

        ┌──────────────────────────────┐
        │ Human Approval Workflow      │
        └──────────────┬───────────────┘
                       ▼

        ┌──────────────────────────────┐
        │ Governance Audit Workflow    │
        └──────────────┬───────────────┘
                       ▼

        ┌──────────────────────────────┐
        │ SharePoint Audit Repository  │
        └──────────────┬───────────────┘
                       ▼

      ┌────────────────┴────────────────┐
      ▼                                 ▼

┌───────────────┐              ┌────────────────┐
│ Teams Alerts  │              │ Email Reports  │
└───────────────┘              └────────────────┘
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
