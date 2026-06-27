import { Circle } from "lucide-react";

export default function Navbar() {
  return (
    <header className="flex h-16 items-center justify-between border-b border-slate-800 bg-slate-950 px-8">
      <div>
        <h2 className="text-xl font-semibold">
          Security Operations Center
        </h2>

        <p className="text-sm text-slate-400">
          Detection Engineering & AI Incident Response
        </p>
      </div>

      <div className="flex items-center gap-2 rounded-full bg-slate-800 px-4 py-2">
        <Circle
          className="fill-green-500 text-green-500"
          size={10}
        />

        <span className="text-sm">
          Backend Online
        </span>
      </div>
    </header>
  );
}