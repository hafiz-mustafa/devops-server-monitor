# 🖥️ Infrastructure Memory Monitoring System (Server Monitor)

A lightweight DevOps-oriented Python script designed to simulate automated cloud infrastructure server checks. This utility monitors memory status by analyzing primary system load alongside containerized environments (Docker), evaluating potential overload risks based on specific threshold limitations.

## 🚀 Key Features Implemented
- **Automated Calculations:** Integrates core programming logic (Integers, Strings, Booleans) to evaluate operational parameters.
- **Dynamic Status Reports:** Formats infrastructure diagnostic metrics dynamically.
- **Risk Assessment Alerts:** Triggers descriptive error logging and warnings if server parameters exceed optimal safety margins.

## 🛠️ Code Logic Structure
The architecture relies on structured, strictly-typed functional checks:
1. `get_total_ram(used, docker)` -> Computes cumulative resource footprint.
2. `get_status_report(server_name, total_ram)` -> Compiles human-readable runtime strings.
3. `is_server_overloaded(total_ram)` -> Evaluates critical threshold status (Flagged at >= 12 GB).

## 📊 Quick Start & Execution

Ensure Python is installed on your local infrastructure environment, then run the script directly from your terminal interface:

```bash
python server_monitor.py
```

### 📋 Expected Output (Threshold Alert Triggered)
```text
============================================================
                INFRASTRUCTURE MONITORING SYSTEM                
============================================================
[METRIC] Total Consumption: 13 GB

[REPORT] Server [DevOps-Prod-Server] current RAM usage is: 13 GB.

[ALERT] Is Server Overloaded?: True
🚨 WARNING: High memory pressure detected! Scalability action required.
============================================================
```

## 📬 Contact & Connect
Built by **Hafiz Mustafa** — Aspiring DevOps Engineer. Feel free to reach out on my [LinkedIn Profile](https://linkedin.com).