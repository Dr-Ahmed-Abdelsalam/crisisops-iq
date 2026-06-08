class CommunicationAgent:
    """
    Generates stakeholder communication drafts.
    """

    def generate(self, crisis_summary: str) -> dict:
        return {
            "executive_update": (
                "Executive Brief: A high-priority crisis has been detected. "
                "Immediate coordination is recommended based on the current severity and policy guidance."
            ),
            "customer_update": (
                "Customer Notice: We are aware of a service disruption affecting some users. "
                "Our teams are actively working on resolution and will provide updates as more information becomes available."
            ),
            "internal_team_update": (
                "Internal Update: Please follow the crisis response workflow, document all actions, "
                "and escalate any high-risk decision for human approval."
            )
        }
