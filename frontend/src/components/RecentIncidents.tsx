interface Incident {
  incident_id: string;
  title: string;
  severity: string;
  affected_user: string;
  alert_count: number;
}

interface Props {
  incidents: Incident[];
}

export default function RecentIncidents({ incidents }: Props) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-4 text-xl font-semibold text-white">
        Recent Incidents
      </h2>

      <table className="w-full">
        <thead className="text-slate-400">
          <tr>
            <th>Title</th>
            <th>Severity</th>
            <th>User</th>
            <th>Alerts</th>
          </tr>
        </thead>

        <tbody>
          {incidents.map((incident) => (
            <tr
              key={incident.incident_id}
              className="border-t border-slate-800"
            >
              <td className="py-3">{incident.title}</td>
              <td>{incident.severity}</td>
              <td>{incident.affected_user}</td>
              <td>{incident.alert_count}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}