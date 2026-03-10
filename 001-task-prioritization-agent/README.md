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