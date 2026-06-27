import { useQuery } from "@tanstack/react-query";

import {
  getRecentAlerts,
  getRecentEvents,
  getRecentIncidents,
} from "@/api/dashboard";

export function useDashboard() {
  const events = useQuery({
    queryKey: ["dashboard-events"],
    queryFn: getRecentEvents,
  });

  const alerts = useQuery({
    queryKey: ["dashboard-alerts"],
    queryFn: getRecentAlerts,
  });

  const incidents = useQuery({
    queryKey: ["dashboard-incidents"],
    queryFn: getRecentIncidents,
  });

  return {
    events,
    alerts,
    incidents,
  };
}