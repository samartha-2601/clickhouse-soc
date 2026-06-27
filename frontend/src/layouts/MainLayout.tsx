import { Outlet } from "react-router-dom";

import Sidebar from "@/components/Sidebar";
import Navbar from "@/components/Navbar";

export default function MainLayout() {
  return (
    <div className="flex h-screen bg-slate-950 text-white">
      <Sidebar />

      <div className="flex flex-1 flex-col overflow-hidden">
        <Navbar />

        <main className="flex-1 overflow-auto bg-slate-900 p-8">
          <Outlet />
        </main>
      </div>
    </div>
  );
}