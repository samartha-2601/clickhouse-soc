import time

from backend.database.repository import EventRepository
from backend.simulator.services.bulk_simulator import BulkSimulator

repo = EventRepository()

sim = BulkSimulator()

events = sim.generate(
    normal_sessions=1000,
    attack_sessions=50,
)

start = time.perf_counter()

repo.insert_events(events)

elapsed = time.perf_counter() - start

print("=" * 60)
print("Bulk Ingestion")
print("=" * 60)

print(f"Events inserted : {len(events)}")
print(f"Time            : {elapsed:.3f} sec")
print(f"Events/sec      : {len(events)/elapsed:,.0f}")