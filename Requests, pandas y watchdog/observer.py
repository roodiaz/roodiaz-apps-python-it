import subprocess
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyEventHandler(FileSystemEventHandler):

    def __init__(self):
        super().__init__()
        self.lastmod = time.perf_counter()

    def on_modified(self, event):
        super().on_modified(event)
        if event.src_path.endswith("productos.xlsx"):
            if time.perf_counter() - self.lastmod > 4:
                print("productos.xlsx modificado, actualizando...")
                subprocess.run(["python", "productos.py"])
                print("Actualizado!")
                self.lastmod = time.perf_counter()


observer = Observer()
observer.schedule(MyEventHandler(), ".", recursive=False)
observer.start()
try:
    while observer.is_alive():
        observer.join(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
