import { api } from "./client";

export async function getAlerts(limit = 100) {
  const response = await api.get("/alerts", {
    params: {
      limit,
    },
  });

  return response.data;
}