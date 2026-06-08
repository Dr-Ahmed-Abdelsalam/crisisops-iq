class ComplianceAgent:
    """
    Reviews legal, compliance, governance, and approval risks.
    """

    def review(self, crisis_data: dict) -> dict:
        approval_required = bool(crisis_data.get("compliance_risk", False))

        return {
            "risk_level": "High" if approval_required else "Medium",
            "human_approval_required": approval_required,
            "sensitive_decisions": [
                "Public customer communication",
                "Regulatory notification",
                "Service shutdown decision",
                "Customer compensation decision"
            ],
            "governance_note": "High-impact actions must be reviewed by a human decision-maker before execution."
        }
