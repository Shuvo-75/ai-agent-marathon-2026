# 🤖 Agent 003: Calendar Conflict Resolver
> **Mission:** An automated agent that scans calendar data to detect overlapping meetings and suggests logical resolutions based on priority and flexibility.

---

### 🎯 Capabilities
* **Overlap Detection:** Identifies events that occupy the same time slot.
* **Buffer Analysis:** Flags events that don't have a minimum 10-minute gap.
* **Smart Resolution:** Suggests which meeting to move based on `priority` and `flexibility` scores.
* **Severity Scoring:** Categorizes conflicts into High or Medium severity.

### 🚀 How to Run
1. Navigate to this folder: `cd 003-calendar-conflict-agent`
2. Run the agent:
   ```bash
   python agent.py