import { api } from "./client";

export async function getIncidents(limit = 100) {
  const response = await api.get("/incidents", {
    params: { limit },
  });

  return response.data;
}

export async function investigateIncident(
  incidentId: string,
) {
  const response = await api.post(
    `/incidents/${incidentId}/investigate`
  );

  return response.data;
}