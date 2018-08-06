#!/usr/bin/python3
# -*- coding: utf-8 -*-
from watchdog.events import *
import requests
import json

def is_ignored(filename):
    # 防止 './ezlab/main.py.20246d7692ece55bd2fa2a37aec9a8ba.py' 这种中间文件的产生
    if '.py.' in filename:
        return True
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

    def deploy_to_esp(self, event, event_type):
        print("==============================================================")
        if event.is_directory:
            file_type = 'directory'
            file_type_cn = '目录'
        else:
            file_type = 'file'
            file_type_cn = '文件'

        if event_type == 'moved':
            print("监测到{0}改动: {1} moved from {2} to {3}".format(
                file_type_cn, file_type, event.src_path, event.dest_path))
            data = dict(event_type='%s_moved' % file_type,
                        filename=event.src_path, dest_path=event.dest_path)

        elif event_type == 'created':
            print("监测到{0}改动: {1} created:{2}".format(
                file_type_cn, file_type, event.src_path))
            data = dict(event_type='%s_created' %
                        file_type, filename=event.src_path)

        elif event_type == 'deleted':
            print("监测到{0}改动: {1} deleted:{2}".format(
                file_type_cn, file_type, event.src_path))
            data = dict(event_type='%s_deleted' %
                        file_type, filename=event.src_path)

        elif event_type == 'modified':
            print("监测到{0}改动: {1} modified:{2}".format(
                file_type_cn, file_type, event.src_path))
            data = dict(event_type='%s_modified' %
                        file_type, filename=event.src_path)

        else:
            pass

        print('正在将改动部署至ESP...')
        req = requests.post('http://%s/change-file/' % self.host, data=data)
        r = json.loads(req.text)
        if r['code'] == 0:
            print('针对于{0}的{1}改动已部署成功!'.format(event.src_path, event_type))
        else:
            print('部署失败.')
        print("==============================================================\n")

    def on_moved(self, event):
        if not is_ignored(event.src_path):
            self.deploy_to_esp(event, 'moved')

    def on_created(self, event):
        if not is_ignored(event.src_path):
            self.deploy_to_esp(event, 'created')

    def on_deleted(self, event):
        if not is_ignored(event.src_path):
            self.deploy_to_esp(event, 'deleted')

    def on_modified(self, event):
        if not is_ignored(event.src_path):
            self.deploy_to_esp(event, 'modified')
