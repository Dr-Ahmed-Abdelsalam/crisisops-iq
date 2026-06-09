import streamlit as st
import pandas as pd
from datetime import datetime


# =============================
# Page Configuration
# =============================

st.set_page_config(
    page_title="CrisisOps IQ",
    page_icon="🚨",
    layout="wide"
)


# =============================
# Helper Functions
# =============================

def load_text_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception:
        return "File not found or could not be loaded."


def calculate_severity(row: pd.Series, meeting_notes: str) -> float:
    score = 4.0

    severity = str(row.get("severity", "")).lower()
    affected_customers = int(row.get("affected_customers", 0))

    if severity == "high":
        score += 2.0
    elif severity == "medium":
        score += 1.0

    if affected_customers >= 1000:
        score += 1.0

    keywords = [
        "compliance",
        "regulatory",
        "customer complaints",
        "executive",
        "escalation",
        "outage"
    ]

    notes_lower = meeting_notes.lower()

    for keyword in keywords:
        if keyword in notes_lower:
            score += 0.4

    return min(round(score, 1), 10.0)


def classify_crisis(row: pd.Series, meeting_notes: str) -> dict:
    text = f"{row.to_dict()} {meeting_notes}".lower()

    if "outage" in text or "service" in text:
        crisis_type = "Service Disruption"
    elif "supply" in text:
        crisis_type = "Supply Chain Disruption"
    elif "compliance" in text or "regulatory" in text:
        crisis_type = "Compliance Incident"
    else:
        crisis_type = "Operational Incident"

    return {
        "crisis_type": crisis_type,
        "affected_customers": int(row.get("affected_customers", 0)),
        "status": row.get("status", "Open")
    }


def approval_required(severity_score: float, meeting_notes: str) -> bool:
    sensitive_terms = [
        "compliance",
        "regulatory",
        "public",
        "customer",
        "executive",
        "notification"
    ]

    return severity_score >= 7 or any(term in meeting_notes.lower() for term in sensitive_terms)


def generate_action_plan(severity_score: float) -> pd.DataFrame:
    if severity_score >= 7:
        rows = [
            ["0-2 hours", "Activate crisis response team", "Operations Team", "High"],
            ["2-4 hours", "Confirm affected services and customer impact", "Operations Team", "High"],
            ["4-6 hours", "Review compliance exposure", "Compliance Team", "High"],
            ["6-12 hours", "Prepare executive and customer communications", "Communications Team", "Medium"],
            ["12-24 hours", "Record decisions in audit log", "Executive Office", "Medium"],
        ]
    else:
        rows = [
            ["0-4 hours", "Monitor incident status", "Operations Team", "Medium"],
            ["4-8 hours", "Collect additional information", "Operations Team", "Medium"],
            ["8-24 hours", "Prepare internal update if needed", "Communications Team", "Low"],
        ]

    return pd.DataFrame(rows, columns=["Timeframe", "Action", "Owner", "Priority"])


def generate_audit_log(case_id: str, severity_score: float, approval: bool) -> pd.DataFrame:
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    rows = [
        [
            case_id,
            "Calculate severity score",
            f"Severity calculated as {severity_score}/10 based on impact, customer exposure, and governance signals.",
            "ESC-SEV-HIGH-002" if severity_score >= 7 else "ESC-SEV-MED-001",
            "No",
            "Completed",
            now
        ],
        [
            case_id,
            "Activate response workflow",
            "Incident requires structured crisis response and executive visibility.",
            "POL-CRISIS-001",
            "Yes" if approval else "No",
            "Pending Approval" if approval else "Approved",
            now
        ],
        [
            case_id,
            "Prepare stakeholder communications",
            "Customer and executive communications should be reviewed before release.",
            "TPL-CUSTOMER-UPDATE-001",
            "Yes",
            "Pending Approval",
            now
        ],
    ]

    return pd.DataFrame(
        rows,
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


# =============================
# Load Demo Data
# =============================

try:
    reports = pd.read_csv("demo_data/crisis_reports.csv")
    resources = pd.read_csv("demo_data/resources.csv")

    meeting_notes = load_text_file("demo_data/meeting_notes.txt")
    crisis_policy = load_text_file("demo_data/crisis_policy.md")
    communication_templates = load_text_file("demo_data/communication_templates.md")
    escalation_rules = load_text_file("demo_data/escalation_rules.md")

except Exception as error:
    st.error(f"Unable to load demo data: {error}")
    st.stop()


# =============================
# Sidebar
# =============================

st.sidebar.title("🚨 CrisisOps IQ")
st.sidebar.caption("Executive Crisis Intelligence Agent")

selected_case_id = st.sidebar.selectbox(
    "Select Crisis Case",
    reports["case_id"].tolist()
)

selected_case = reports[reports["case_id"] == selected_case_id].iloc[0]

st.sidebar.divider()
st.sidebar.markdown("### Microsoft IQ Layer")
st.sidebar.info("Foundry IQ concept integration using synthetic policy knowledge.")

st.sidebar.markdown("### Responsible AI Notice")
st.sidebar.warning("Synthetic demo data only. Do not upload confidential or personal information.")


# =============================
# Analysis
# =============================

classification = classify_crisis(selected_case, meeting_notes)
severity_score = calculate_severity(selected_case, meeting_notes)
needs_approval = approval_required(severity_score, meeting_notes)

action_plan = generate_action_plan(severity_score)
audit_log = generate_audit_log(selected_case_id, severity_score, needs_approval)


# =============================
# Main Interface
# =============================

st.title("🚨 CrisisOps IQ")
st.subheader("Executive Crisis Intelligence Agent for Microsoft 365 Copilot")

st.markdown(
    """
CrisisOps IQ transforms scattered crisis reports, meeting notes, operational data,
and enterprise policies into a governed executive response plan.
"""
)

st.divider()


# =============================
# Executive Metrics
# =============================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Severity Score", f"{severity_score}/10")

with col2:
    st.metric("Crisis Type", classification["crisis_type"])

with col3:
    st.metric("Status", classification["status"])

with col4:
    st.metric("Human Approval", "Required" if needs_approval else "Not Required")

st.divider()


# =============================
# Crisis Summary
# =============================

st.header("1. Crisis Summary")

st.write(
    f"""
The selected crisis case **{selected_case_id}** has been classified as a
**{classification["crisis_type"]}**.

The incident involves potential operational disruption, stakeholder impact,
and governance considerations. Based on the available synthetic crisis reports
and meeting notes, CrisisOps IQ recommends structured response planning,
executive visibility, and controlled stakeholder communications.
"""
)

with st.expander("View synthetic crisis reports"):
    st.dataframe(reports, use_container_width=True)

with st.expander("View meeting notes"):
    st.text(meeting_notes)


# =============================
# Foundry IQ Concept Layer
# =============================

st.header("2. Foundry IQ Concept Layer")

st.info(
    """
In this hackathon demo, Foundry IQ is represented through a synthetic governed
knowledge layer containing crisis policies, escalation rules, communication
templates, and compliance guidance.
"""
)

policy_col, rules_col = st.columns(2)

with policy_col:
    with st.expander("Crisis Policy"):
        st.markdown(crisis_policy)

with rules_col:
    with st.expander("Escalation Rules"):
        st.markdown(escalation_rules)


# =============================
# Root Cause Analysis
# =============================

st.header("3. Root Cause Analysis & Priority Ranking")

st.markdown(
    """
### Likely Root Cause

- Partial operational disruption affecting customer-facing services.
- Delayed internal escalation and increased support pressure.
- Rising customer complaints and potential governance exposure.
- Need for executive coordination and controlled communications.

### Priority Ranking

1. Confirm incident scope and affected users.
2. Activate the crisis response workflow.
3. Assign operational and executive owners.
4. Review compliance and approval requirements.
5. Prepare approved stakeholder communications.
"""
)


# =============================
# Action Plan
# =============================

st.header("4. 24-Hour Action Plan")

st.dataframe(action_plan, use_container_width=True)


# =============================
# Resource Allocation
# =============================

st.header("5. Resource Allocation")

st.dataframe(resources, use_container_width=True)


# =============================
# Communications
# =============================

st.header("6. Stakeholder Communications")

with st.expander("Executive Update"):
    st.write(
        """
A high-priority operational incident has been identified. The response team is
assessing operational impact, customer exposure, and compliance implications.
Immediate executive visibility and approval are recommended for external communications.
"""
    )

with st.expander("Customer Update"):
    st.write(
        """
We are aware of a service disruption affecting some users. Our teams are actively
working to resolve the issue and will provide updates as more information becomes available.
"""
    )

with st.expander("Internal Team Update"):
    st.write(
        """
Please follow the crisis response workflow. Document all actions, escalate sensitive
decisions, and ensure that customer-facing communications are approved before release.
"""
    )

with st.expander("Communication Templates"):
    st.markdown(communication_templates)


# =============================
# Compliance Review
# =============================

st.header("7. Legal & Compliance Risk Layer")

if needs_approval:
    st.warning(
        """
Potential compliance or governance exposure exists. Any public statement,
regulatory notification, customer compensation decision, or legal admission
requires human approval before release.
"""
    )
else:
    st.success(
        """
No immediate high-risk compliance trigger detected from the available synthetic inputs.
Continue monitoring and document all response actions.
"""
    )


# =============================
# Human Approval Gates
# =============================

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


# =============================
# Audit Log
# =============================

st.header("9. Audit Log")

st.dataframe(audit_log, use_container_width=True)


# =============================
# Final Note
# =============================

st.success("CrisisOps IQ working demo completed successfully.")

st.caption(
    "This demo uses synthetic or redacted data only. It is not a replacement for legal, compliance, operational, or executive judgment."
)
