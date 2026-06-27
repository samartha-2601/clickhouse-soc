import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

import SeverityBadge from "@/components/common/SeverityBadge";
import StatusBadge from "@/components/common/StatusBadge";

interface Alert {
  alert_id: string;
  rule_name: string;
  severity: string;
  status: string;
  username: string;
  host: string;
  event_count: number;
  mitre_technique: string;
}

interface Props {
  alerts: Alert[];
}

export default function AlertTable({
  alerts,
}: Props) {
  return (
    <div className="rounded-xl border border-slate-800">
      <Table>
        <TableHeader className="bg-slate-900">
          <TableRow>
            <TableHead className="font-semibold text-slate-300">Rule</TableHead>
            <TableHead className="font-semibold text-slate-300">Severity</TableHead>
            <TableHead className="font-semibold text-slate-300">Status</TableHead>
            <TableHead className="font-semibold text-slate-300">User</TableHead>
            <TableHead className="font-semibold text-slate-300">Host</TableHead>
            <TableHead className="font-semibold text-slate-300">Events</TableHead>
            <TableHead className="font-semibold text-slate-300">MITRE</TableHead>
          </TableRow>
        </TableHeader>

        <TableBody>
          {alerts.map((alert) => (
            <TableRow className="hover:bg-slate-800/40 transition-colors" key={alert.alert_id}>
              <TableCell>{alert.rule_name}</TableCell>
              <TableCell>
                <SeverityBadge
                    severity={alert.severity}
                />
              </TableCell>
              <TableCell>
                <StatusBadge
                    status={alert.status}
                />
              </TableCell>
              <TableCell>{alert.username}</TableCell>
              <TableCell>{alert.host}</TableCell>
              <TableCell>{alert.event_count}</TableCell>
              <TableCell>{alert.mitre_technique}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}