from backend.simulator.services.event_factory import EventFactory


class AdministratorGenerator:

    @staticmethod
    def maintenance(session):

        return [

            EventFactory.create_event(
                session,
                "successful_login",
                message="Administrator logged in"
            ),

            EventFactory.create_event(
                session,
                "ssh",
                message="SSH session established"
            ),

            EventFactory.create_event(
                session,
                "sudo",
                severity="medium",
                message="sudo executed"
            ),

            EventFactory.create_event(
                session,
                "system_update",
                severity="medium",
                message="System packages updated"
            ),

            EventFactory.create_event(
                session,
                "logout",
                message="Administrator logged out"
            ),
        ]