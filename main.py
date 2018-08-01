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
        # your own code
        pass
