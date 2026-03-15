import csv
import json
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import List

PRIORITY_MAP = {"low": 1, "medium": 2, "high": 3}
BUFFER_MINUTES = 10  # Minimum gap required between events

@dataclass
class Event:
    title: str
    start: datetime
    end: datetime
    priority: int
    event_type: str
    flexible: bool

def parse_datetime(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d %H:%M")

def read_calendar(path="calendar.csv") -> List[Event]:
    events = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            events.append(Event(
                title=row["title"],
                start=parse_datetime(row["start_time"]),
                end=parse_datetime(row["end_time"]),
                priority=PRIORITY_MAP[row["priority"].lower()],
                event_type=row["type"],
                flexible=row["flexible"].lower() == "yes"
            ))
    return sorted(events, key=lambda e: e.start)

def detect_conflicts(events: List[Event]):
    conflicts = []
    for i in range(len(events) - 1):
        a = events[i]
        b = events[i + 1]

        # Check if events overlap
        overlap = a.end > b.start
        # Check if there is enough buffer time
        no_buffer = (b.start - a.end) < timedelta(minutes=BUFFER_MINUTES)

        if overlap or no_buffer:
            conflict_type = "overlap" if overlap else "no_buffer"
            severity = "high" if a.priority == 3 or b.priority == 3 else "medium"
            suggestion = suggest_resolution(a, b)

            conflicts.append({
                "event_a": a.title,
                "event_b": b.title,
                "type": conflict_type,
                "severity": severity,
                "suggestion": suggestion
            })
    return conflicts

def suggest_resolution(a: Event, b: Event) -> str:
    if a.priority > b.priority and b.flexible:
        return f"Reschedule '{b.title}' (Lower priority & flexible)"
    if b.priority > a.priority and a.flexible:
        return f"Reschedule '{a.title}' (Lower priority & flexible)"
    if a.flexible and b.flexible:
        return "Both are flexible. Shorten or reschedule either."
    return "Crucial conflict: Requires human intervention."

def main():
    events = read_calendar()
    conflicts = detect_conflicts(events)

    # Save outputs
    with open("conflicts.json", "w", encoding="utf-8") as f:
        json.dump(conflicts, f, indent=2)

    with open("conflicts.txt", "w", encoding="utf-8") as f:
        f.write("Calendar Conflict Report\n")
        f.write("=" * 40 + "\n\n")
        for c in conflicts:
            f.write(f"- Conflict between '{c['event_a']}' and '{c['event_b']}'\n")
            f.write(f"  Type: {c['type']}, Severity: {c['severity']}\n")
            f.write(f"  Suggested Action: {c['suggestion']}\n\n")

    print(f"Analysis complete. Detected {len(conflicts)} conflicts.")
    print("Check conflicts.txt for details.")

if __name__ == "__main__":
    main()