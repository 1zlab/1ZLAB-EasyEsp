from watchdog.observers import Observer
from watchdog.events import *
import requests
import time
import json
import sys


def is_ignored(filename):

    with open('./.ezignore', 'r') as f:
        ignored_files = f.read().split('\n')
    for i in ignored_files:
        if i:
            if i.endswith('/'):
                if filename.startswith('./'+i):
                    return True
                    
            elif filename == './'+i:
                return True

    return False


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, host):
        FileSystemEventHandler.__init__(self)
        self.host = host

    def on_moved(self, event):
        if not is_ignored(event.src_path):
            if event.is_directory:
                print("directory moved from {0} to {1}".format(
                    event.src_path, event.dest_path))

                data = dict(event_type='directory_moved', filename=event.src_path,
                            dest_path=event.dest_path)
                requests.post('http://%s/change-file/' % self.host, data=data)

            else:
                print("file moved from {0} to {1}".format(
                    event.src_path, event.dest_path))
                data = dict(event_type='file_moved', filename=event.src_path,
                            dest_path=event.dest_path)
                requests.post('http://%s/change-file/' % self.host, data=data)

    def on_created(self, event):
        if not is_ignored(event.src_path):
            if event.is_directory:
                print("directory created:{0}".format(event.src_path))

                data = dict(event_type='directory_created',
                            filename=event.src_path)
                requests.post('http://%s/change-file/' % self.host, data=data)

            else:
                print("file created:{0}".format(event.src_path))
                data = dict(event_type='file_created', filename=event.src_path)
                requests.post('http://%s/change-file/' % self.host, data=data)

    def on_deleted(self, event):
        if not is_ignored(event.src_path):
            if event.is_directory:
                print("directory deleted:{0}".format(event.src_path))
                data = dict(event_type='directory_deleted',
                            filename=event.src_path)
                requests.post('http://%s/change-file/' % self.host, data=data)

            else:
                print("file deleted:{0}".format(event.src_path))
                data = dict(event_type='file_deleted', filename=event.src_path)
                requests.post('http://%s/change-file/' % self.host, data=data)

    def on_modified(self, event):
        if not is_ignored(event.src_path):
            if event.is_directory:
                print("directory modified:{0}".format(event.src_path))
                # data = dict(event_type='directory_modified',
                #             filename=event.src_path)
                # requests.post('http://%s/change-file/' % self.host, data=data)

            else:
                with open(event.src_path, 'r') as f:
                    content = f.read()
                print("file modified:{0}".format(event.src_path))
                data = dict(event_type='file_modified',
                            filename=event.src_path, content=content)
                requests.post('http://%s/change-file/' % self.host, data=data)


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
