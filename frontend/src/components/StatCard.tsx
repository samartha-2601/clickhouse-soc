import { ReactNode } from "react";

interface Props {
  title: string;
  value: number | string;
  subtitle: string;
  icon: ReactNode;
}

export default function StatCard({
  title,
  value,
  subtitle,
  icon,
}: Props) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6 transition-all duration-200 hover:border-blue-500/40 hover:shadow-lg hover:shadow-blue-900/20">
      <div className="flex items-start justify-between">

        <div>

          <p className="text-sm text-slate-400">
            {title}
          </p>

          <h2 className="mt-2 text-4xl font-bold">
            {value}
          </h2>

          <p className="mt-2 text-sm text-slate-500">
            {subtitle}
          </p>

        </div>

        <div className="rounded-lg bg-blue-500/10 p-3 text-blue-400">
          {icon}
        </div>

      </div>
    </div>
  );
}