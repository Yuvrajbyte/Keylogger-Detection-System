# 🔐 Keylogger Detection System (Behavior-Based)

## 📌 Overview
This project implements a **behavior-based keylogger detection system** using Python. Instead of creating or interacting with a keylogger, the system focuses on **detecting suspicious behavior** that may indicate the presence of a keylogger.

The detection logic is inspired by real-world **Endpoint Detection and Response (EDR)** tools, which rely on correlating multiple weak signals rather than signature-based detection.

---

## 🎯 Objective
To identify **potential keylogger activity** by monitoring:
- Suspicious running processes
- Abnormal file system write behavior
- Correlating these signals into a risk score

The system classifies threats into **LOW, MEDIUM, or HIGH** risk levels.

---

## 🧠 How It Works (Architecture)

```
┌──────────────────────┐
│  Process Monitor     │
│  (psutil)            │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  File Monitor        │
│  (watchdog)          │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Risk Engine         │
│  (Heuristic Scoring) │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Alert & Logging     │
│  (LOW / MED / HIGH) │
└──────────────────────┘
```

---

## 📂 Project Structure

```
keylogger_detection/
│
├── main.py                # Main controller
├── process_monitor.py     # Suspicious process detection
├── file_monitor.py        # File write activity monitoring
├── risk_engine.py         # Risk scoring logic
├── logs/
│   └── alerts.log         # Detection logs
└── README.md
```

---

## 🔍 Detection Logic

### 1️⃣ Process Monitoring
- Scans **all running processes** on the system
- Flags processes with suspicious keywords such as:
  - `keylog`
  - `keyboard`
  - `hook`
  - `logger`
  - `capture`

### 2️⃣ File Activity Monitoring
- Monitors a specified directory for **real-time file modifications**
- Focuses on file types commonly used by keyloggers:
  - `.txt`, `.log`, `.dat`

### 3️⃣ Risk Scoring Engine
The system assigns risk based on:
- Number of suspicious processes detected
- Frequency of file write events

#### Risk Levels
| Score Range | Threat Level |
|-----------|--------------|
| 0–3 | LOW |
| 4–7 | MEDIUM |
| 8+ | HIGH |

---

## 🧪 Example Output

```
===== KEYLOGGER DETECTION REPORT =====
Suspicious Processes: []
File Write Events: ['test.txt']
Risk Score: 2
Threat Level: LOW
```

---

## 🛠️ Technologies Used
- **Python 3.11**
- **psutil** – process monitoring
- **watchdog** – file system monitoring

---

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install psutil watchdog
   ```
3. Run the program:
   ```bash
   python main.py
   ```
4. Create or modify `.txt` / `.log` files in the monitored directory during execution

---

## ⚠️ Limitations
- Does not capture actual keystrokes (by design)
- Detection is heuristic-based, not signature-based
- May generate false positives in high file-activity environments

---

## 🎓 Learning Outcomes
- Understanding of behavior-based malware detection
- Practical exposure to process and file monitoring
- Risk-based threat classification
- Modular security tool design

---

## 📜 Disclaimer
This project is strictly for **educational and defensive cybersecurity purposes**. It does **not** create, deploy, or assist in building keyloggers.

---

## 👤 Author
**[Yuvraj Singh]**  
Cybersecurity Student | Python Developer

