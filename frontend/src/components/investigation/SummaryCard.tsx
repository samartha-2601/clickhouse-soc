interface Props {
  title: string;
  content: string;
}

export default function SummaryCard({
  title,
  content,
}: Props) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-3 text-lg font-semibold">
        {title}
      </h2>

      <p className="text-slate-300 whitespace-pre-wrap">
        {content}
      </p>
    </div>
  );
}