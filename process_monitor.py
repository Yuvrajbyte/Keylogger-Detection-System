import psutil

SUSPICIOUS_KEYWORDS = [
    "keylog", "keyboard", "hook", "logger", "capture"
]

def scan_processes():
    hits = []

    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name']
            if name:
                lname = name.lower()
                for keyword in SUSPICIOUS_KEYWORDS:
                    if keyword in lname:
                        hits.append(name)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    return hits
