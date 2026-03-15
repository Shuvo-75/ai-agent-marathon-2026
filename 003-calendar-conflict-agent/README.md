# 🗓️ Agent 003: Calendar Conflict Resolver
> **Mission:** An automated scheduling intelligence tool designed to analyze temporal overlaps, enforce transition buffers, and provide logical resolution strategies for overbooked calendars.

---

### 🎯 Key Capabilities
* **Intersection Analysis:** Scans your `calendar.csv` to find direct time overlaps between scheduled events.
* **Buffer Enforcement:** Automatically flags "Back-to-Back" fatigue by ensuring a minimum **10-minute transition window** between tasks.
* **Smart Resolution Engine:** Suggests the best course of action by weighing **Priority** (High/Med/Low) against **Flexibility** (Yes/No).
* **Severity Tiering:** Categorizes conflicts into `High` or `Medium` severity to help you focus on the most critical schedule breaks first.
* **Automated Reporting:** Exports findings into structured `JSON` and a clean `TXT` summary for quick review.

---

### 🛠️ Technical Specifications
* **Core Engine:** Python 3.x (utilizing `dataclasses` and `datetime` objects)
* **Data Schema:** CSV-based event ingestion
* **Logic Model:** Deterministic priority-based decision tree
* **Output:** `conflicts.json`, `conflicts.txt`

---

### 🚀 Quick Start

1.  **Enter the Agent's Workspace:**
    ```powershell
    cd 003-calendar-conflict-agent
    ```

2.  **Input Your Schedule:**
    Open `calendar.csv` and populate it with your meetings. Ensure the `flexible` column is set correctly (`yes`/`no`) to guide the resolution logic.

3.  **Run the Analysis:**
    ```powershell
    python agent.py
    ```

4.  **Analyze Results:**
    * Open **`conflicts.txt`** for a human-readable summary of what to reschedule.
    * Open **`conflicts.json`** for structured data integration.

---

### ⚙️ Conflict Resolution Logic

The agent evaluates every pair of consecutive events ($E_1, E_2$) using a strict temporal logic:

#### **1. Detection Formula**
A conflict is flagged if:
$$(Start_{E2} < End_{E1}) \lor (Start_{E2} - End_{E1} < 10min)$$

#### **2. Decision Matrix**
The suggestion engine follows this hierarchy:

| Condition | Suggested Action |
| :--- | :--- |
| $Priority_1 > Priority_2$ & $E_2$ is Flexible | **Reschedule $E_2$** |
| $Priority_2 > Priority_1$ & $E_1$ is Flexible | **Reschedule $E_1$** |
| Both Events are Flexible | **Shorten or Reschedule one** |
| Both are High Priority/Fixed | **Manual Intervention Required** |

---

### 📂 Repository Structure
* `agent.py` — The logic controller and parser.
* `calendar.csv` — Your raw event data.
* `conflicts.json` — Machine-readable output.
* `conflicts.txt` — Formatted human-readable report.