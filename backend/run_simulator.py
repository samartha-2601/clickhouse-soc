import time

from backend.database.client import get_client
from backend.database.repository import EventRepository
from backend.simulator.services.bulk_simulator import BulkSimulator


def main():

    print("=" * 70)
    print("ClickHouse SOC - Enterprise Simulator")
    print("=" * 70)

    client = get_client()

    print("\nCleaning security_events table...")

    client.command("TRUNCATE TABLE security_events")
    client.command("TRUNCATE TABLE security_alerts")
    client.command("TRUNCATE TABLE security_incidents")

    simulator = BulkSimulator()

    print("Generating enterprise activity...")

    events = simulator.generate(
        normal_sessions=1000,
        attack_sessions=50,
    )

    print(f"Generated {len(events)} events")

    repo = EventRepository()

    start = time.perf_counter()

    repo.insert_events(events)

    elapsed = time.perf_counter() - start

    print("\nBulk ingestion complete")

    print(f"Insert Time : {elapsed:.3f} sec")
    print(f"Events/sec  : {len(events)/elapsed:,.0f}")

    result = client.query(
        "SELECT COUNT(*) AS total FROM security_events"
    )

    total = result.result_rows[0][0]

    print(f"Database Rows : {total}")

    print("\nSimulator completed successfully.")


if __name__ == "__main__":
    main()