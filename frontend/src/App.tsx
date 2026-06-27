import { Routes, Route, Navigate } from "react-router-dom";

import MainLayout from "@/layouts/MainLayout";

import Dashboard from "@/pages/Dashboard/Dashboard";
import Events from "@/pages/Events/Events";
import Alerts from "@/pages/Alerts/Alerts";
import Incidents from "@/pages/Incidents/Incidents";
import Investigation from "@/pages/Investigation/Investigation";

export default function App() {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<Navigate to="/dashboard" replace />} />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/events"
          element={<Events />}
        />

        <Route
          path="/alerts"
          element={<Alerts />}
        />

        <Route
          path="/incidents"
          element={<Incidents />}
        />

        <Route
          path="/investigation/:id"
          element={<Investigation />}
        />
      </Route>
    </Routes>
  );
}