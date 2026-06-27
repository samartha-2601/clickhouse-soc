import json


class PromptBuilder:

    def build(
        self,
        incident: dict,
        alerts: list,
        events: list,
    ) -> str:

        timeline = []

        for event in events:

            timeline.append(
                {
                    "timestamp": str(event["timestamp"]),
                    "event_type": event["event_type"],
                    "severity": event["severity"],
                    "message": event["message"],
                    "host": event["host"],
                    "username": event["username"],
                }
            )

        evidence = {
            "incident": incident,
            "alerts": alerts,
            "timeline": timeline,
        }

        evidence_json = json.dumps(
            evidence,
            indent=2,
            default=str,
        )

        return f"""
You are a Senior Incident Response Engineer.

Analyze the supplied security incident.

Return ONLY valid JSON.

Return this exact schema:

{{
  "executive_summary": "",
  "technical_summary": "",
  "root_cause": "",
  "mitre_analysis": "",
  "timeline": [
    {{
      "timestamp": "",
      "event": ""
    }}
  ],
  "containment": [],
  "remediation": [],
  "confidence": 0.0
}}

Security Evidence

{evidence_json}
"""