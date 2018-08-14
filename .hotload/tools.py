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
        print('\033[1;31;40mconnecting to network...\033[0m')
        wlan.connect(wifi_name, wifi_pwd)
        
        while not wlan.isconnected():
            import time
            time.sleep(5)
            if not wlan.isconnected():
                wlan.active(False)
                print("\033[1;31;40mWifi connection error,please reset the wifi config\033[0m") 

                from tools import wifi_config
                wifi_config()
                break
            else:            
                print('\033[1;31;40mNetwork Config: \033[0m', wlan.ifconfig())
                print('\033[1;31;40mESP32 IP: \033[0m', wlan.ifconfig()[0])

    if is_developing:
        print('\033[1;31;40mDevelope Mode Enabled.\033[0m')
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

    print('\033[1;31;40mwifi config changed. to apply the changes you made, please reboot\033[0m')


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
                clear(path+'/'+i)
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


