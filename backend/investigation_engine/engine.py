from backend.database.alert_repository import AlertRepository
from backend.database.repository import EventRepository
from backend.database.incident_repository import IncidentRepository
from backend.database.investigation_repository import InvestigationRepository

from backend.investigation_engine.openai_client import OpenAIClient
from backend.investigation_engine.prompt_builder import PromptBuilder
from backend.investigation_engine.service import InvestigationService


class InvestigationEngine:

    def __init__(self):

        self.incidents = IncidentRepository()

        self.alerts = AlertRepository()

        self.events = EventRepository()

        self.openai = OpenAIClient()

        self.prompts = PromptBuilder()

        self.service = InvestigationService()

        self.repository = InvestigationRepository()

    def investigate(
        self,
        incident_id: str,
    ):

        # --------------------------------------------------
        # Load Incident
        # --------------------------------------------------

        incident = self.incidents.get_incident(
            incident_id,
        )

        if incident is None:
            return None

        # --------------------------------------------------
        # Load Related Alerts
        # --------------------------------------------------

        alerts = self.alerts.get_alerts_for_incident(
            incident["affected_user"],
            incident["affected_host"],
        )

        # --------------------------------------------------
        # Load Related Events
        # --------------------------------------------------

        events = self.events.get_events_for_incident(
            incident["affected_user"],
            incident["affected_host"],
        )

        # --------------------------------------------------
        # Build Prompt
        # --------------------------------------------------

        prompt = self.prompts.build(
            incident,
            alerts,
            events,
        )

        # --------------------------------------------------
        # OpenAI Investigation
        # --------------------------------------------------

        investigation_json = self.openai.investigate(
            prompt,
        )

        # --------------------------------------------------
        # Build Investigation Model
        # --------------------------------------------------

        investigation = self.service.build(
            incident,
            investigation_json,
        )

        # --------------------------------------------------
        # Persist Investigation
        # --------------------------------------------------

        self.repository.insert_investigation(
            investigation,
        )

        return investigation