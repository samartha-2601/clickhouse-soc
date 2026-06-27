interface Props {
  status: string;
}

export default function StatusBadge({
  status,
}: Props) {
  const open =
    status.toUpperCase() === "OPEN";

  return (
    <span
      className={`rounded-full px-3 py-1 text-xs font-semibold ${
        open
          ? "bg-blue-500/20 text-blue-300 border border-blue-500/30"
          : "bg-green-500/20 text-green-300 border border-green-500/30"
      }`}
    >
      {status}
    </span>
  );
}