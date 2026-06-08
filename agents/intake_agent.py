class IntakeAgent:
    """
    Intake Agent
    Reads crisis reports, meeting notes, and operational updates,
    then extracts the key facts needed for crisis analysis.
    """

    def process(self, report_text: str, meeting_notes: str = "") -> dict:
        combined_text = f"{report_text}\n{meeting_notes}".lower()

        affected_customers = "customer" in combined_text or "complaint" in combined_text
        service_issue = "outage" in combined_text or "service" in combined_text
        compliance_risk = "compliance" in combined_text or "regulatory" in combined_text

        return {
            "crisis_type": "Service Disruption" if service_issue else "Operational Incident",
            "affected_customers": affected_customers,
            "compliance_risk": compliance_risk,
            "source_summary": "Crisis report and meeting notes processed successfully."
        }
