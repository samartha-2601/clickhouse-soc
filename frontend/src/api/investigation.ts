import { api } from "./client";

export async function investigateIncident(
  incidentId: string,
) {
  const response = await api.post(
    `/incidents/${incidentId}/investigate`
  );

  return response.data;
}