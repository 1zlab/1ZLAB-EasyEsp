from microWebSrv import MicroWebSrv
import json


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
        with open(filename, 'w') as f:
            f.write(formData['content'])

    content = json.dumps(dict(code=0, message='%s hotload done.' % filename))
    httpResponse.WriteResponseOk(headers=None,
                                 contentType="text/html",
                                 contentCharset="UTF-8",
                                 content=content)


hotloader = MicroWebSrv()
