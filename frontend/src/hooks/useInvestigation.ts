import { useQuery } from "@tanstack/react-query";

import { investigateIncident } from "@/api/investigation";

export function useInvestigation(
  incidentId: string,
) {
  return useQuery({
    queryKey: [
      "investigation",
      incidentId,
    ],

    queryFn: () =>
      investigateIncident(
        incidentId,
      ),

    enabled: !!incidentId,
  });
}