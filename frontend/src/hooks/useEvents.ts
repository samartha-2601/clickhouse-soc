import { useQuery } from "@tanstack/react-query";

import { getEvents } from "@/api/events";
import type { EventFilters } from "@/api/events";

export function useEvents(filters: EventFilters) {
  return useQuery({
    queryKey: ["events", filters],
    queryFn: () => getEvents(filters),
  });
}