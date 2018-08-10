import network
import json
import socket
import os


def load_config():
    with open('/hotload/config.json', 'r') as f:
        config = json.loads(f.read())

    wifi_name = config['wifi_name']
    wifi_pwd = config['wifi_pwd']
    # 是否为开发模式
    is_developing = config['is_developing']
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(wifi_name, wifi_pwd)
        for i in range(3):
            if not wlan.isconnected():
                pass
    print('network config:', wlan.ifconfig())
    if is_developing:
        print('Develope Mode Enabled.')

        return True
    else:
        return False


def wifi_config():
    wifi_name = input('wifi name: ')
    wifi_pwd = input('password: ')
    with open('/hotload/config.json', 'r') as f:
        config = json.loads(f.read())

    config['wifi_name'] = wifi_name
    config['wifi_pwd'] = wifi_pwd

    with open('/hotload/config.json', 'w') as f:
        f.write(json.dumps(config))


def clear(path='/'):
    warning = input(
        'Do you really want to remove all python codes from esp32?[y/n]')
    if warning == 'y' or warning == 'yes':
        for i in os.listdir(path):
            if i == 'boot.py':
                continue
            try:
                os.remove(path+'/'+i)
            except:
                clear_up(path+'/'+i)
        os.rmdir(path)


def is_developing():
    with open('/hotload/config.json', 'r') as f:
        config = json.loads(f.read())

    is_developing = config['is_developing']

    if is_developing:
        config['is_developing'] = 0
    else:
        config['is_developing'] = 1

    with open('/hotload/config.json', 'w') as f:
        f.write(json.dumps(config))


def find_host():
    import urequests
    for i in range(1, 255):
        for j in range(1, 255):
            try:
                r = urequests.get('http://192.168.%s.%s:5000/' % i % j)
                if r.text:
                    print(r.text)
                    break
            except:
                # print('no host response')
                pass
        break