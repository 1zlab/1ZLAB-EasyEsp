from watchdog.events import *
import requests
import threading




class FileEventHandler(FileSystemEventHandler):
    def __init__(self, host):
        FileSystemEventHandler.__init__(self)
        self.host = host

    def on_moved(self, event):
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

        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
            data = dict(event_type='directory_modified',
                        filename=event.src_path)
            requests.post('http://%s/change-file/' % self.host, data=data)

        else:
            with open(event.src_path, 'r') as f:
                content = f.read()
            print("file modified:{0}".format(event.src_path))
            data = dict(event_type='file_modified',
                            filename=event.src_path, content=content)
            requests.post('http://%s/change-file/' % self.host, data=data)
