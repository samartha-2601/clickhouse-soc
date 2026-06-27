from datetime import timedelta

from backend.simulator.services.event_factory import EventFactory


class SSHBruteForceCampaign:

    @staticmethod
    def execute(session, start_time):

        events = []

        current = start_time

        # Five failed logins
        for _ in range(5):

            events.append(

                EventFactory.create_event(
                    session=session,
                    event_type="failed_login",
                    severity="medium",
                    message="Failed SSH login",
                    mitre_tactic="Credential Access",
                    mitre_technique="T1110",
                    timestamp=current,
                )
            )

            current += timedelta(seconds=5)

        # Successful login
        events.append(

            EventFactory.create_event(
                session=session,
                event_type="successful_login",
                severity="medium",
                message="Successful SSH login",
                timestamp=current,
            )
        )

        current += timedelta(seconds=10)

        # Privilege escalation
        events.append(

            EventFactory.create_event(
                session=session,
                event_type="sudo",
                severity="high",
                message="Privilege escalation using sudo",
                mitre_tactic="Privilege Escalation",
                mitre_technique="T1548",
                timestamp=current,
            )
        )

        return events