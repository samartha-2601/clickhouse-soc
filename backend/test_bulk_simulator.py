from collections import Counter

from backend.simulator.services.bulk_simulator import BulkSimulator

sim = BulkSimulator()

events = sim.generate()

print("=" * 60)
print("Simulation Results")
print("=" * 60)

print()

print(f"Total Events: {len(events)}")

counter = Counter(event.event_type for event in events)

print()

for event_type, count in sorted(counter.items()):
    print(f"{event_type:20} {count}")