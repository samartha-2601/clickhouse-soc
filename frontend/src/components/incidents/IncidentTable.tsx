import { useNavigate } from "react-router-dom";

import { Button } from "@/components/ui/button";

import SeverityBadge from "@/components/common/SeverityBadge";
import StatusBadge from "@/components/common/StatusBadge";

interface Incident {
  incident_id: string;
  title: string;
  severity: string;
  status: string;
  affected_user: string;
  affected_host: string;
  alert_count: number;
}

interface Props {
  incidents: Incident[];
}

export default function IncidentTable({
  incidents,
}: Props) {
  const navigate = useNavigate();

  return (
    <div className="rounded-xl border border-slate-800 overflow-hidden">
      <table className="w-full">
        <thead className="bg-slate-900">
          <tr>
            <th className="p-3 text-left">Title</th>
            <th className="p-3 text-left">Severity</th>
            <th className="p-3 text-left">Status</th>
            <th className="p-3 text-left">User</th>
            <th className="p-3 text-left">Host</th>
            <th className="p-3 text-left">Alerts</th>
            <th className="p-3 text-left">Action</th>
          </tr>
        </thead>

        <tbody>
          {incidents.map((incident) => (
            <tr
              key={incident.incident_id}
              className="hover:bg-slate-800/40 transition-colors"
            >
              <td className="p-3">
                {incident.title}
              </td>

              <td><SeverityBadge
                severity={incident.severity}
                /></td>

              <td><StatusBadge
                status={incident.status}
                /></td>

              <td>{incident.affected_user}</td>

              <td>{incident.affected_host}</td>

              <td>{incident.alert_count}</td>

              <td>
                <Button
                  onClick={() =>
                    navigate(
                      `/investigation/${incident.incident_id}`
                    )
                  }
                >
                  Investigate
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}