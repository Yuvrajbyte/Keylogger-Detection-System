import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileWriteHandler(FileSystemEventHandler):
    def __init__(self):
        self.events = []

    def on_modified(self, event):
        if not event.is_directory:
            if event.src_path.endswith((".txt", ".log", ".dat")):
                self.events.append(event.src_path)

def monitor_files(path=".", duration=60):
    print(f"[DEBUG] Monitoring folder: {path}")
    print(f"[DEBUG] Duration: {duration} seconds")

    handler = FileWriteHandler()
    observer = Observer()
    observer.schedule(handler, path, recursive=True)
    observer.start()

    time.sleep(duration)

    observer.stop()
    observer.join()

    return handler.events
