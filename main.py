import network
import json

def load_config():
    with open('./esp_config.json','r') as f:
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
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    if is_developing:
        print('Develope Mode Enabled.')
        return True
    else:
        return False


if __name__ == '__main__':
    
    if load_config():
        from hotload import hotloader
        hotloader.Start()
    else:
        # your own code 
        pass