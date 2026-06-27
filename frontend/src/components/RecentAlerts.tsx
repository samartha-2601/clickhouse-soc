interface Alert {
  alert_id: string;
  rule_name: string;
  severity: string;
  username: string;
  host: string;
}

interface Props {
  alerts: Alert[];
}

export default function RecentAlerts({ alerts }: Props) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-4 text-xl font-semibold text-white">
        Recent Alerts
      </h2>

      <table className="w-full text-left">
        <thead className="text-slate-400">
          <tr>
            <th>Rule</th>
            <th>Severity</th>
            <th>User</th>
            <th>Host</th>
          </tr>
        </thead>

        <tbody>
          {alerts.map((alert) => (
            <tr
              key={alert.alert_id}
              className="border-t border-slate-800"
            >
              <td className="py-3">{alert.rule_name}</td>
              <td>{alert.severity}</td>
              <td>{alert.username}</td>
              <td>{alert.host}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}