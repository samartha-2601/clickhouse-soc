from backend.simulator.services.event_factory import EventFactory


class AuthenticationGenerator:

    @staticmethod
    def developer_login(session):

        return [
            EventFactory.create_event(
                session,
                "successful_login",
                message="Developer logged in"
            ),

            EventFactory.create_event(
                session,
                "git_pull",
                message="Git repository updated"
            ),

            EventFactory.create_event(
                session,
                "logout",
                message="Developer logged out"
            )
        ]