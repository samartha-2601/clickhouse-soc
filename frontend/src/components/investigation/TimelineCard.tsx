interface TimelineEvent {
  timestamp: string;
  event: string;
}

interface Props {
  timeline: string;
}

export default function TimelineCard({
  timeline,
}: Props) {
  let events: TimelineEvent[] = [];

  try {
    events = JSON.parse(timeline);
  } catch {
    events = [];
  }

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-4 text-lg font-semibold">
        Attack Timeline
      </h2>

      <div className="space-y-4">
        {events.map((item, index) => (
          <div
            key={index}
            className="border-l-2 border-blue-500 pl-4"
          >
            <p className="text-sm text-slate-400">
              {item.timestamp}
            </p>

            <p className="text-white">
              {item.event}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}