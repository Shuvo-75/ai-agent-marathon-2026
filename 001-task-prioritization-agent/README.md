# 🤖 Agent 001: Daily Task Prioritization Agent
> **Mission:** A smart CLI tool designed to analyze a task list (`tasks.csv`) and generate an optimized daily plan based on effort, impact, and deadlines.

---

### 🎯 Capabilities
* **Data Normalization:** Automatically converts human-readable effort labels (e.g., `S, M, L`) into precise time estimates in minutes.
* **Weighted Scoring:** Calculates priority scores using a multi-factor decision matrix including Urgency, Importance, and Quick-win bonuses.
* **Task Categorization:** Dynamically segments tasks into `TOP 3` (Immediate focus), `NEXT 5` (Secondary), and `DEFER` (Low urgency/impact) groups.
* **Dual-Format Output:** Generates `plan.json` for automation and `plan.txt` for human readability.

---

### 🛠️ Tech Stack
* **Language:** Python 3 (Standard Library)
* **Input Format:** CSV
* **Output Formats:** JSON, TXT

---

### 🚀 Quick Start Guide

1. **Navigate to the agent directory:**
   ```powershell
   cd 001-task-prioritization-agent

2. **Configure your tasks:** Open and edit the `tasks.csv` file with your specific tasks, deadlines (`YYYY-MM-DD`), and impact levels (`low`, `medium`, `high`).

3. **Execute the Agent:**
   Run the script using the following command in your terminal:
   ```powershell
   python agent.py

4. **Review your Plan:**
   Check the output files to see your prioritized schedule:
   * **`plan.txt`**: Human-readable view of your schedule.
   * **`plan.json`**: Raw data for automation or further processing.

   ## ⚙️ Scoring Logic
The agent utilizes a deterministic scoring algorithm to eliminate decision fatigue and prioritize high-value tasks:

$$Score = (Urgency \times 2.0) + (Importance \times 3.0) + QuickWin - BlockedPenalty$$

* **Urgency:** Higher weight for tasks with closer deadlines or overdue status.
* **Importance:** Scaled based on impact level (**High = 3**, **Medium = 2**, **Low = 1**).
* **Quick Win:** **1.0 point bonus** for tasks requiring $\leq 15$ minutes of effort.
* **Blocked Penalty:** **-5.0 point penalty** for tasks marked as 'blocked', pushing them to the bottom of the list until resolved.
