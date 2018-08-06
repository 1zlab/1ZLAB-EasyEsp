# -*- coding:utf-8 -*-
from watchdog.observers import Observer
from libs.handler import FileEventHandler
import fire
import time
import json
import sys
import os


class EzEsp(object):

    def hotload(self, path, host):
        host = host
        observer = Observer()
        event_handler = FileEventHandler(host)
        observer.schedule(event_handler, path, True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

    def deploy(self, com, srcpath):
        for i in os.listdir(srcpath):
            print(
                'excuting:sudo ampy -p {0} put {1}/{2}'.format(com, srcpath, i))
            os.system('sudo ampy -p {0} put {1}/{2}'.format(com, srcpath, i))
        print('DONE.\nPLEASE REBOOT THE MACHINE TWICE,THEN YOU CAN USE HOTLOAD.')


if __name__ == "__main__":
    fire.Fire(EzEsp)
