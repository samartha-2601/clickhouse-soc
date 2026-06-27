import {
  Activity,
  ShieldAlert,
  TriangleAlert,
} from "lucide-react";

import StatCard from "@/components/StatCard";

import RecentAlerts from "@/components/RecentAlerts";
import RecentEvents from "@/components/RecentEvents";
import RecentIncidents from "@/components/RecentIncidents";

import { useDashboard } from "@/hooks/useDashboard";

export default function Dashboard() {
  const {
    events,
    alerts,
    incidents,
  } = useDashboard();

  if (
    events.isLoading ||
    alerts.isLoading ||
    incidents.isLoading
  ) {
    return (
      <div className="flex h-64 items-center justify-center">
        <p className="text-slate-400">
          Loading dashboard...
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-8">

      {/* Header */}

      <div>
        <h1 className="text-4xl font-bold text-white">
          Security Dashboard
        </h1>

        <p className="mt-2 text-slate-400">
          Real-time overview of security events,
          alerts, incidents and AI investigations.
        </p>
      </div>

      {/* KPI Cards */}

      <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">

        <StatCard
          title="Events"
          value={events.data?.length ?? 0}
          subtitle="Latest security telemetry"
          icon={<Activity size={24} />}
        />

        <StatCard
          title="Alerts"
          value={alerts.data?.length ?? 0}
          subtitle="Detection engine findings"
          icon={<TriangleAlert size={24} />}
        />

        <StatCard
          title="Incidents"
          value={incidents.data?.length ?? 0}
          subtitle="Correlated security incidents"
          icon={<ShieldAlert size={24} />}
        />

      </div>

      {/* Dashboard Sections */}

      <RecentAlerts
        alerts={alerts.data ?? []}
      />

      <RecentIncidents
        incidents={incidents.data ?? []}
      />

      <RecentEvents
        events={events.data ?? []}
      />

    </div>
  );
}