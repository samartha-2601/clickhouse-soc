import { api } from "./client";

export interface EventFilters {
  username?: string;
  host?: string;
  severity?: string;
  event_type?: string;
  limit?: number;
  offset?: number;
}

export async function getEvents(filters: EventFilters) {
  const response = await api.get("/events", {
    params: filters,
  });

  return response.data;
}