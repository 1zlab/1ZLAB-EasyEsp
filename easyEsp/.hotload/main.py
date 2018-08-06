# -*- coding:utf-8 -*-
import os


if __name__ == '__main__':
    print('init machine...')
    files = os.listdir()
    os.mkdir('ezlab')
    for i in files:
        if not i == 'main.py' and not i == 'boot.py':
            os.rename(i, '/ezlab/%s' % i)
    main_code = """
import network
import json
import sys


if __name__ == '__main__':
    # 添加ezlab包路径  add module ezlab to path 
    sys.path.append('ezlab')
    from tools import load_config
    # 是否开启热加载    hotloader mode or not
    if load_config():
        from hotload import hotloader
        hotloader().Start()
    else:
        # your own code goes here
        pass
"""
    with open('main.py', 'w') as f:
        f.write(main_code)

    print('init done,please reboot the machine.')
