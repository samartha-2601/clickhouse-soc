interface Event {
  event_id: string;
  timestamp: string;
  event_type: string;
  username: string;
  host: string;
}

interface Props {
  events: Event[];
}

export default function RecentEvents({ events }: Props) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-4 text-xl font-semibold text-white">
        Recent Events
      </h2>

      <table className="w-full">
        <thead className="text-slate-400">
          <tr>
            <th>Time</th>
            <th>Event</th>
            <th>User</th>
            <th>Host</th>
          </tr>
        </thead>

        <tbody>
          {events.map((event) => (
            <tr
              key={event.event_id}
              className="border-t border-slate-800"
            >
              <td className="py-3">
                {new Date(event.timestamp).toLocaleTimeString()}
              </td>
              <td>{event.event_type}</td>
              <td>{event.username}</td>
              <td>{event.host}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}