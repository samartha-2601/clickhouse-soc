from backend.database.client import get_client

client = get_client()

print("=" * 50)

print("Connected to ClickHouse!")

print(client.command("SELECT version()"))

print("=" * 50)