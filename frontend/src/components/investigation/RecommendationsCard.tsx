interface Props {
  title: string;
  content: string;
}

export default function RecommendationsCard({
  title,
  content,
}: Props) {
  let recommendations: string[] = [];

  try {
    recommendations = JSON.parse(content);
  } catch {
    recommendations = [];
  }

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-4 text-lg font-semibold">
        {title}
      </h2>

      <ul className="space-y-2">
        {recommendations.map((item, index) => (
          <li
            key={index}
            className="text-slate-300"
          >
            • {item}
          </li>
        ))}
      </ul>
    </div>
  );
}