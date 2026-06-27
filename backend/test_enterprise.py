from backend.simulator.services.simulator import build_demo_enterprise

enterprise = build_demo_enterprise()

print(f"Enterprise: {enterprise.name}")

print("\nUsers")

for user in enterprise.users:
    print(user)

print("\nHosts")

for host in enterprise.hosts:
    print(host)