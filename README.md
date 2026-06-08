# CrisisOps IQ

## Executive Crisis Intelligence Agent for Microsoft 365 Copilot

CrisisOps IQ is an Executive Crisis Intelligence Agent designed for the **Enterprise Agents** track of the Microsoft Agents League Hackathon.

The project is designed to support organizations during operational disruptions, compliance incidents, customer escalations, supply chain failures, and service outages by transforming scattered crisis reports, meeting notes, operational signals, and internal policies into a governed executive response plan.

CrisisOps IQ focuses on:

- crisis analysis,
- severity scoring,
- policy-grounded recommendations,
- stakeholder communications,
- compliance review,
- human approval gates,
- and audit-ready decision records.

---

## Hackathon Track

**Track:** Enterprise Agents  
**Target Environment:** Microsoft 365 Copilot Chat  
**Microsoft IQ Layer:** Foundry IQ concept integration  
**Project Type:** Executive crisis response and governance agent

---

## Problem Statement

Organizations often struggle to respond effectively during crises because critical information is fragmented across reports, meetings, emails, operational systems, and policy documents.

During a crisis, decision-makers need to quickly understand:

- what happened,
- who is affected,
- how severe the situation is,
- what policies apply,
- what actions should be prioritized,
- what communications are required,
- and which decisions require human approval.

Without a structured response process, organizations may face delayed decisions, inconsistent communication, compliance risks, and weak accountability.

---

## Proposed Solution

CrisisOps IQ consolidates crisis-related information and turns it into an executive-ready response package.

The agent analyzes synthetic crisis reports, meeting notes, operational data, and policy documents to produce:

- a crisis summary,
- a severity score,
- likely root cause analysis,
- priority ranking,
- a 24-hour response plan,
- resource allocation guidance,
- stakeholder communication drafts,
- legal and compliance risk notes,
- human approval gates,
- and an audit log explaining each recommendation.

---

## Microsoft IQ Integration

CrisisOps IQ is designed to integrate with **Microsoft Foundry IQ** as its governed enterprise knowledge layer.

In this hackathon demo, Foundry IQ concepts are represented through a synthetic policy repository containing:

- crisis management policies,
- escalation rules,
- communication templates,
- compliance guidance,
- and operational playbooks.

This design demonstrates how an enterprise agent can retrieve relevant organizational knowledge and generate grounded, policy-aware recommendations.

Future production versions may connect Foundry IQ directly to enterprise repositories such as SharePoint, OneDrive, Microsoft 365 knowledge sources, or approved internal policy systems.

---

## Microsoft 365 Copilot Alignment

CrisisOps IQ is designed as a Microsoft 365 Copilot Chat agent experience.

A crisis manager or executive user can interact with the agent conversationally by asking questions such as:

- “Summarize the current crisis.”
- “What is the severity level?”
- “Which policies apply?”
- “What should we do in the next 24 hours?”
- “Which actions require human approval?”
- “Draft an update for executives and customers.”

This aligns with the Enterprise Agents challenge by extending Microsoft 365 Copilot into a real-world business scenario involving crisis response, governance, and executive decision support.

---

## Core Capabilities

### 1. Crisis Summary

Generates an executive-ready summary of the crisis from multiple synthetic inputs.

### 2. Severity Score

Assesses the crisis level using operational impact, customer impact, compliance exposure, urgency, and resource constraints.

### 3. Root Cause Analysis

Identifies likely contributing causes and uncertainty factors.

### 4. Priority Ranking

Ranks urgent response actions by operational importance and governance risk.

### 5. 24-Hour Action Plan

Creates a practical short-term response plan for the first 24 hours.

### 6. Resource Allocation

Suggests how available teams and resources should be assigned.

### 7. Stakeholder Communications

Drafts communications for:

- executive leadership,
- internal teams,
- customers,
- partners,
- and public-facing updates when appropriate.

### 8. Legal & Compliance Risk Layer

Highlights sensitive decisions, compliance risks, notification duties, and governance concerns.

### 9. Human Approval Gates

Prevents high-impact recommendations from being treated as automatic actions.

Examples of actions requiring human approval:

- public statements,
- customer compensation,
- regulatory notifications,
- service shutdown decisions,
- legal admissions,
- and major resource reallocations.

### 10. Audit Log

Records:

- recommendation,
- reasoning,
- supporting policy reference,
- risk level,
- approval requirement,
- and timestamp.

---

## Multi-Agent Design

CrisisOps IQ is structured around specialized agent roles:

1. **Intake Agent**  
   Extracts key facts from crisis reports and meeting notes.

2. **Crisis Classifier Agent**  
   Identifies crisis type, affected stakeholders, severity, and urgency.

3. **Knowledge Retrieval Agent**  
   Retrieves relevant policies, escalation rules, and templates from the synthetic Foundry IQ-style knowledge layer.

4. **Operations Planner Agent**  
   Builds the 24-hour action plan and resource allocation recommendations.

5. **Legal & Compliance Agent**  
   Reviews sensitive decisions, compliance risks, and approval requirements.

6. **Communications Agent**  
   Generates stakeholder-ready communications.

7. **Verifier & Safety Agent**  
   Checks that recommendations are explainable, policy-aware, and do not bypass human approval.

---

## Responsible AI & Safety

CrisisOps IQ is designed with safety and governance as core requirements.

The system does not automatically execute sensitive operational, legal, financial, or public-facing actions.

Instead, it:

- flags high-risk decisions,
- requires human approval,
- explains recommendation logic,
- references applicable policy categories,
- avoids using confidential or personal data,
- and maintains audit-ready records.

The project is a hackathon demo and is not a replacement for professional legal, compliance, operational, or executive judgment.

---

## Data Protection Notice

This demo uses synthetic or redacted data only.

Do not upload:

- confidential information,
- personal data,
- customer data,
- employee data,
- privileged legal documents,
- passwords,
- API keys,
- tokens,
- `.env` files,
- or production configurations.

---

## Demo Scenario

The initial demo scenario focuses on an enterprise service disruption involving:

- rising customer complaints,
- delayed internal response,
- potential compliance exposure,
- resource constraints,
- and the need for executive communication.

CrisisOps IQ converts the scattered crisis information into a governed executive response plan.

---

## Technology Stack

- Microsoft 365 Copilot Chat concept
- Microsoft Foundry IQ concept integration
- Python
- Streamlit
- Retrieval-Augmented Generation pattern
- Synthetic enterprise crisis data
- Markdown-based policy repository

---

## Planned Repository Structure

```text
crisisops-iq/
│
├── app.py
├── requirements.txt
│
├── agents/
│   ├── intake_agent.py
│   ├── classifier_agent.py
│   ├── retrieval_agent.py
│   ├── planner_agent.py
│   ├── compliance_agent.py
│   └── communication_agent.py
│
├── demo_data/
│   ├── crisis_reports.csv
│   ├── resources.csv
│   ├── meeting_notes.txt
│   ├── crisis_policy.md
│   ├── communication_templates.md
│   └── escalation_rules.md
│
├── docs/
│   ├── architecture.md
│   ├── responsible_ai.md
│   └── audit_log_example.md
│
└── README.md
```

---

## Hackathon Evaluation Alignment

CrisisOps IQ is designed to align with the judging criteria:

### Accuracy & Relevance

Addresses a real enterprise crisis management problem and aligns with the Enterprise Agents track.

### Reasoning & Multi-Step Thinking

Uses a multi-agent workflow to move from intake to classification, policy retrieval, planning, compliance review, communication, approval, and audit logging.

### Creativity & Originality

Positions the agent as an executive crisis intelligence layer rather than a generic chatbot or document assistant.

### User Experience & Presentation

Provides an executive-ready dashboard and conversational Copilot-style experience.

### Reliability & Safety

Includes human approval gates, audit logging, responsible AI notices, synthetic data, and governance-first design.

### Community Value

Demonstrates how AI agents can help organizations respond faster and more responsibly during critical situations.

---

## Current Status

Project page created.  
Repository initialized.  
README drafted.  
Synthetic demo data and MVP implementation are in progress.

---

## Disclaimer

CrisisOps IQ is a hackathon prototype.

It is not a production system and should not be used as a substitute for professional crisis management, legal advice, compliance review, or executive decision-making.

All demo materials use synthetic or redacted data only.
