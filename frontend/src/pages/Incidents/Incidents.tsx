import IncidentTable from "@/components/incidents/IncidentTable";
import { useIncidents } from "@/hooks/useIncidents";

export default function Incidents() {
  const { data, isLoading } = useIncidents();

  if (isLoading) {
    return (
      <div className="text-white">
        Loading incidents...
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold">
          Security Incidents
        </h1>

        <p className="text-slate-400">
          Correlated incidents ready for investigation.
        </p>
      </div>

      <IncidentTable
        incidents={data ?? []}
      />
    </div>
  );
}