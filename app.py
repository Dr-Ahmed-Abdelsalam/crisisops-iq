import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="CrisisOps IQ",
    page_icon="🚨",
    layout="wide"
)

# -----------------------------
# Helper functions
# -----------------------------

def load_text_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception:
        return "File not found or could not be loaded."


def calculate_severity(row):
    base_score = 5

    severity = str(row.get("severity", "")).lower()
    affected_customers = int(row.get("affected_customers", 0))

    if severity == "high":
        base_score += 2
    elif severity == "medium":
        base_score += 1

    if affected_customers > 1000:
        base_score += 1

    return min(base_score, 10)


def approval_required(severity_score):
    return severity_score >= 7


# -----------------------------
# Load demo data
# -----------------------------

reports = pd.read_csv("demo_data/crisis_reports.csv")
resources = pd.read_csv("demo_data/resources.csv")

meeting_notes = load_text_file("demo_data/meeting_notes.txt")
crisis_policy = load_text_file("demo_data/crisis_policy.md")
communication_templates = load_text_file("demo_data/communication_templates.md")
escalation_rules = load_text_file("demo_data/escalation_rules.md")

main_case = reports.iloc[0]
severity_score = calculate_severity(main_case)
requires_approval = approval_required(severity_score)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("CrisisOps IQ")
st.sidebar.markdown("Executive Crisis Intelligence Agent")
st.sidebar.divider()

selected_case = st.sidebar.selectbox(
    "Select crisis case",
    reports["case_id"].tolist()
)

st.sidebar.markdown("### Microsoft IQ Layer")
st.sidebar.info("Foundry IQ concept integration using synthetic policy knowledge.")

st.sidebar.markdown("### Safety Notice")
st.sidebar.warning("Synthetic demo data only. Do not upload confidential or personal information.")

# -----------------------------
# Main page
# -----------------------------

st.title("🚨 CrisisOps IQ")
st.subheader("Executive Crisis Intelligence Agent for Microsoft 365 Copilot")

st.markdown(
    """
CrisisOps IQ transforms scattered crisis reports, meeting notes, operational data,
and enterprise policies into a governed executive response plan.
"""
)

st.divider()

# -----------------------------
# Executive metrics
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Severity Score", f"{severity_score}/10")

with col2:
    st.metric("Crisis Type", "Service Disruption")

with col3:
    st.metric("Status", str(main_case.get("status", "Open")))

with col4:
    st.metric("Human Approval", "Required" if requires_approval else "Not Required")

st.divider()

# -----------------------------
# Crisis Summary
# -----------------------------

st.header("1. Crisis Summary")

st.write(
    """
The selected crisis involves a customer service platform disruption with rising customer complaints,
operational pressure on support teams, and potential compliance exposure due to delayed notification.

The incident requires immediate executive awareness, coordinated operational response, and controlled
stakeholder communications.
"""
)

# -----------------------------
# Data view
# -----------------------------

with st.expander("View synthetic crisis reports"):
    st.dataframe(reports, use_container_width=True)

with st.expander("View meeting notes"):
    st.text(meeting_notes)

# -----------------------------
# Foundry IQ concept layer
# -----------------------------

st.header("2. Foundry IQ Concept Layer")

st.info(
    """
In this demo, Foundry IQ is represented through a synthetic governed knowledge layer containing
crisis policies, escalation rules, communication templates, and compliance guidance.
"""
)

col_a, col_b = st.columns(2)

with col_a:
    with st.expander("Crisis Policy"):
        st.markdown(crisis_policy)

with col_b:
    with st.expander("Escalation Rules"):
        st.markdown(escalation_rules)

# -----------------------------
# Root cause and priority
# -----------------------------

st.header("3. Root Cause Analysis & Priority Ranking")

st.markdown(
    """
### Likely Root Cause

- Partial platform outage affecting customer service operations.
- Delayed internal escalation.
- Increasing customer complaints and support workload.
- Potential gap in timely stakeholder notification.

### Priority Ranking

1. Confirm incident scope and affected users.
2. Activate crisis response team.
3. Assign operational and executive owners.
4. Review compliance and communication requirements.
5. Prepare approved stakeholder communications.
"""
)

# -----------------------------
# 24-hour action plan
# -----------------------------

st.header("4. 24-Hour Action Plan")

action_plan = pd.DataFrame(
    [
        ["0-2 hours", "Activate crisis response team", "Operations Team", "High"],
        ["2-4 hours", "Confirm customer impact and service scope", "Operations Team", "High"],
        ["4-6 hours", "Review compliance exposure", "Compliance Team", "High"],
        ["6-12 hours", "Prepare customer and executive updates", "Communications Team", "Medium"],
        ["12-24 hours", "Document actions in audit log", "Executive Office", "Medium"],
    ],
    columns=["Timeframe", "Action", "Owner", "Priority"]
)

st.dataframe(action_plan, use_container_width=True)

# -----------------------------
# Resource allocation
# -----------------------------

st.header("5. Resource Allocation")

st.dataframe(resources, use_container_width=True)

# -----------------------------
# Communications
# -----------------------------

st.header("6. Stakeholder Communications")

with st.expander("Executive Update"):
    st.write(
        """
A high-priority operational incident has been identified affecting the customer service platform.
The crisis response team is assessing operational impact, customer exposure, and compliance implications.
Immediate executive visibility and approval are recommended for external communications.
"""
    )

with st.expander("Customer Update"):
    st.write(
        """
We are aware of a service disruption affecting some users. Our teams are actively working to resolve
the issue and will provide updates as more information becomes available.
"""
    )

with st.expander("Internal Team Update"):
    st.write(
        """
Please follow the crisis response workflow. Document all actions, escalate sensitive decisions,
and ensure that customer-facing communications are approved before release.
"""
    )

with st.expander("Communication Templates"):
    st.markdown(communication_templates)

# -----------------------------
# Compliance review
# -----------------------------

st.header("7. Legal & Compliance Risk Layer")

st.warning(
    """
Potential compliance exposure exists because customer notification may be delayed.
Any public statement, regulatory notification, customer compensation decision, or legal admission
requires human approval before release.
"""
)

# -----------------------------
# Human approval gates
# -----------------------------

st.header("8. Human Approval Gates")

approval_items = pd.DataFrame(
    [
        ["Public customer communication", "Required", "Executive Office"],
        ["Regulatory notification", "Required", "Compliance Team"],
        ["Customer compensation", "Required", "Executive Office"],
        ["Service shutdown decision", "Required", "Operations + Executive Office"],
        ["Internal operational update", "Not Required", "Operations Team"],
    ],
    columns=["Decision", "Approval Status", "Approval Owner"]
)

st.dataframe(approval_items, use_container_width=True)

# -----------------------------
# Audit log
# -----------------------------

st.header("9. Audit Log")

audit_log = pd.DataFrame(
    [
        [
            "CASE-1001",
            "Activate crisis response team",
            "High severity incident with customer impact",
            "POL-CRISIS-001",
            "Yes",
            "Pending Approval",
            datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        ],
        [
            "CASE-1001",
            "Prepare customer communication",
            "Customer-facing update requires controlled release",
            "TPL-CUSTOMER-UPDATE-001",
            "Yes",
            "Pending Approval",
            datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        ],
    ],
    columns=[
        "Case ID",
        "Recommendation",
        "Reasoning",
        "Policy Reference",
        "Human Approval Required",
        "Status",
        "Timestamp"
    ]
)

st.dataframe(audit_log, use_container_width=True)

st.success("CrisisOps IQ demo completed successfully.")
