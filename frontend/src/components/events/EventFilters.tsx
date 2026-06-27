import { Input } from "@/components/ui/input";

interface Props {
  username: string;
  host: string;
  severity: string;
  eventType: string;

  setUsername: (v: string) => void;
  setHost: (v: string) => void;
  setSeverity: (v: string) => void;
  setEventType: (v: string) => void;
}

export default function EventFilters({
  username,
  host,
  severity,
  eventType,
  setUsername,
  setHost,
  setSeverity,
  setEventType,
}: Props) {
  return (
    <div className="grid grid-cols-4 gap-4">
      <Input
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <Input
        placeholder="Host"
        value={host}
        onChange={(e) => setHost(e.target.value)}
      />

      <Input
        placeholder="Severity"
        value={severity}
        onChange={(e) => setSeverity(e.target.value)}
      />

      <Input
        placeholder="Event Type"
        value={eventType}
        onChange={(e) => setEventType(e.target.value)}
      />
    </div>
  );
}