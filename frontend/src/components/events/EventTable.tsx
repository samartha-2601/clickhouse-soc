import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

import SeverityBadge from "@/components/common/SeverityBadge";

interface Event {
  event_id: string;
  timestamp: string;
  event_type: string;
  severity: string;
  username: string;
  host: string;
  source_ip: string;
  mitre_technique: string;
}

interface Props {
  events: Event[];
}

export default function EventTable({
  events,
}: Props) {
  return (
    <div className="rounded-xl border border-slate-800">
      <Table>
        <TableHeader className="bg-slate-900">
          <TableRow>
            <TableHead>Time</TableHead>
            <TableHead>Event</TableHead>
            <TableHead>Severity</TableHead>
            <TableHead>User</TableHead>
            <TableHead>Host</TableHead>
            <TableHead>Source IP</TableHead>
            <TableHead>MITRE</TableHead>
          </TableRow>
        </TableHeader>

        <TableBody>
          {events.map((event) => (
            <TableRow className="hover:bg-slate-800/40 transition-colors" key={event.event_id}>
              <TableCell>
                {new Date(
                  event.timestamp
                ).toLocaleString()}
              </TableCell>

              <TableCell>
                {event.event_type}
              </TableCell>

              <TableCell>
                <SeverityBadge
                    severity={event.severity}
                />
              </TableCell>

              <TableCell>
                {event.username}
              </TableCell>

              <TableCell>
                {event.host}
              </TableCell>

              <TableCell>
                {event.source_ip}
              </TableCell>

              <TableCell>
                {event.mitre_technique}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}