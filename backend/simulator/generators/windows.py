from backend.simulator.services.event_factory import EventFactory


class WindowsGenerator:

    @staticmethod
    def office_user(session):

        return [

            EventFactory.create_event(
                session,
                "successful_login",
                message="Windows user logged in"
            ),

            EventFactory.create_event(
                session,
                "powershell",
                message="PowerShell launched"
            ),

            EventFactory.create_event(
                session,
                "outlook",
                message="Outlook opened"
            ),

            EventFactory.create_event(
                session,
                "logout",
                message="Windows user logged out"
            ),
        ]