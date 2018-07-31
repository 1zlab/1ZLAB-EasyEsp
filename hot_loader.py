from watchdog.observers import Observer
from watchdog.events import *
from handler import FileEventHandler
# from flask import Flask
import time
import json
import sys

default_path = '.'

 
if __name__ == "__main__":
    default_path = sys.argv[1]
    host = sys.argv[2]
    observer = Observer()
    event_handler = FileEventHandler(host)
    observer.schedule(event_handler, default_path, True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    # observer.join()   
