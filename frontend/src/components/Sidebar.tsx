import { Shield, LayoutDashboard, Activity, TriangleAlert, Siren, Brain } from "lucide-react";
import { NavLink } from "react-router-dom";

const menu = [
  {
    name: "Dashboard",
    icon: LayoutDashboard,
    path: "/dashboard",
  },
  {
    name: "Events",
    icon: Activity,
    path: "/events",
  },
  {
    name: "Alerts",
    icon: TriangleAlert,
    path: "/alerts",
  },
  {
    name: "Incidents",
    icon: Siren,
    path: "/incidents",
  },
];

export default function Sidebar() {
  return (
    <aside className="flex h-screen w-64 flex-col border-r border-slate-800 bg-slate-950">
      <div className="flex items-center gap-3 border-b border-slate-800 p-6">
        <Shield className="h-8 w-8 text-blue-500" />

        <div>
          <h1 className="text-lg font-bold">
            ClickHouse SOC
          </h1>

          <p className="text-sm text-slate-400">
            AI Security Platform
          </p>
        </div>
      </div>

      <nav className="flex-1 px-4 py-6">
        {menu.map((item) => {
          const Icon = item.icon;

          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                `mb-2 flex items-center gap-3 rounded-lg px-4 py-3 transition ${
                  isActive
                    ? "bg-blue-600 text-white"
                    : "text-slate-300 hover:bg-slate-800"
                }`
              }
            >
              <Icon size={20} />

              {item.name}
            </NavLink>
          );
        })}
      </nav>

      <div className="border-t border-slate-800 p-6">
        <div className="flex items-center gap-3">
          <Brain className="text-green-500" />

          <div>
            <p className="font-medium">
              AI Investigation
            </p>

            <p className="text-xs text-slate-400">
              GPT-4.1 Enabled
            </p>
          </div>
        </div>
      </div>
    </aside>
  );
}