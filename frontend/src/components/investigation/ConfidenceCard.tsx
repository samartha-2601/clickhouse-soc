interface Props {
  confidence: number;
}

export default function ConfidenceCard({
  confidence,
}: Props) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-4 text-lg font-semibold">
        AI Confidence
      </h2>

      <div className="text-4xl font-bold text-green-400">
        {(confidence * 100).toFixed(0)}%
      </div>
    </div>
  );
}