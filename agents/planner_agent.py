class OperationsPlannerAgent:
    """
    Builds a 24-hour executive response plan for the crisis.
    """

    def create_plan(self, severity: str) -> dict:
        if severity.lower() == "high":
            return {
                "priority": "Immediate executive response required",
                "actions": [
                    "Activate crisis response team",
                    "Confirm affected services and customer impact",
                    "Assign operations owner",
                    "Prepare stakeholder communications",
                    "Review compliance and approval requirements"
                ],
                "timeframe": "First 24 hours"
            }

        return {
            "priority": "Standard operational monitoring",
            "actions": [
                "Monitor incident status",
                "Collect additional information",
                "Prepare internal update"
            ],
            "timeframe": "First 24 hours"
        }
