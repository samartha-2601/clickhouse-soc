import { useState } from "react";

import EventFilters from "@/components/events/EventFilters";
import EventTable from "@/components/events/EventTable";

import { useEvents } from "@/hooks/useEvents";

export default function Events() {
  const [username, setUsername] = useState("");
  const [host, setHost] = useState("");
  const [severity, setSeverity] = useState("");
  const [eventType, setEventType] = useState("");

  const { data, isLoading } = useEvents({
    username: username || undefined,
    host: host || undefined,
    severity: severity || undefined,
    event_type: eventType || undefined,
    limit: 100,
    offset: 0,
  });

  if (isLoading) {
    return (
      <div className="text-white">
        Loading...
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold">
          Security Events
        </h1>

        <p className="text-slate-400">
          Search and investigate security events.
        </p>
      </div>

      <EventFilters
        username={username}
        host={host}
        severity={severity}
        eventType={eventType}
        setUsername={setUsername}
        setHost={setHost}
        setSeverity={setSeverity}
        setEventType={setEventType}
      />

      <EventTable
        events={data ?? []}
      />
    </div>
  );
}