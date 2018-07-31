from microWebSrv import MicroWebSrv
import network
import json


def do_connect():
    # import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ChinaNet-Q5uk', '0921608677')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


@MicroWebSrv.route('/')
def homepage(httpClient, httpResponse):
    print('homepage visited!')
    content = json.dumps(
        dict(code=0, message='hello from micropython server!'))
    httpResponse.WriteResponseOk(headers=None,
                                 contentType="text/html",
                                 contentCharset="UTF-8",
                                 content=content)


@MicroWebSrv.route('/change-file', 'POST')
def handleChange(httpClient, httpResponse):
    formData = httpClient.ReadRequestPostedFormData()
    event_type = formData['event_type']
    filename = formData['filename']
    # content = formData['content']

    if event_type == 'file_modified':
        with open(filename,'w') as f:
            f.write(formData['content'])

    content = json.dumps(dict(code=0, message='%s hotload done.' % filename))
    httpResponse.WriteResponseOk(headers=None,
                                 contentType="text/html",
                                 contentCharset="UTF-8",
                                 content=content)


if __name__ == '__main__':
    # print('1st hotload')
    do_connect()
    mws = MicroWebSrv()  # TCP port 80 and files in
    mws.Start()         # Starts server in a new thread
