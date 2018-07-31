import network
import urequests
import json
import socket


def do_connect(wifi_name, wifi_pwd):
    # import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(wifi_name, wifi_pwd)
        print('network config:', wlan.ifconfig())

    return wlan.isconnected()


def get_config():
    with open('./esp_config.json', 'r') as file:
        config = json.loads(file.read())

    wifi_name = config['wifi_name']
    wifi_pwd = config['wifi_pwd']
    is_developing = config['is_developing']
    port = config['port']

    return wifi_name, wifi_pwd, is_developing, port



if __name__ == '__main__':

    wifi_name, wifi_pwd, is_developing, host, port = get_config()

    if do_connect(wifi_name, wifi_pwd):

        r = urequests.get("http://"+host+':'+port+'/is_there_any_changes/')

        if json.loads(r.text)['code'] == 0:
            pass

        print('Waiting for connection...')
        while is_developing == 1:

            is_developing = get_config()[2]

    else:
        print('wifi connection error, please check your wifi settings.')
