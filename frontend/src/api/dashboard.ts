import { api } from "./client";

export async function getRecentEvents() {
  const response = await api.get("/events?limit=5");
  return response.data;
}

export async function getRecentAlerts() {
  const response = await api.get("/alerts?limit=5");
  return response.data;
}

export async function getRecentIncidents() {
  const response = await api.get("/incidents?limit=5");
  return response.data;
}