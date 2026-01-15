from process_monitor import scan_processes
from file_monitor import monitor_files
from risk_engine import calculate_risk
from datetime import datetime
import os

def log_alert(message):
    os.makedirs("logs", exist_ok=True)  
    with open("logs/alerts.log", "a") as f:
        f.write(message + "\n")

def main():
    print("[*] Scanning processes...")
    process_hits = scan_processes()

    print("[*] Monitoring file activity...")
    file_events = monitor_files(path=r"C:\Python Projects\.vscode\keylogger detection",duration=60)

    score, level = calculate_risk(process_hits, file_events)

    print("\n===== KEYLOGGER DETECTION REPORT =====")
    print("Suspicious Processes:", process_hits)
    print("File Write Events:", file_events)
    print("Risk Score:", score)
    print("Threat Level:", level)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_alert(f"[{timestamp}] Score={score} Level={level}")

if __name__ == "__main__":
    main()

