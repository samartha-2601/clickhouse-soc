interface Props {
  severity: string;
}

export default function SeverityBadge({
  severity,
}: Props) {
  const value = severity.toLowerCase();

  const colors = {
    critical:
      "bg-red-600/20 text-red-400 border border-red-500/30",

    high:
      "bg-orange-500/20 text-orange-300 border border-orange-500/30",

    medium:
      "bg-yellow-500/20 text-yellow-300 border border-yellow-500/30",

    low:
      "bg-green-500/20 text-green-300 border border-green-500/30",
  };

  return (
    <span
      className={`rounded-full px-3 py-1 text-xs font-semibold ${
        colors[value as keyof typeof colors] ??
        colors.low
      }`}
    >
      {severity}
    </span>
  );
}