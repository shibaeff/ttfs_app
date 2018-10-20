from datetime import datetime


def application(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    url = environ["HTTP_HOST"]+environ["PATH_INFO"]
    data = ('{{time: {}, url: {}}}'.format(datetime.now(), url)).encode()
    response_headers = [
        ('Content-type', 'application/json'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    
    return iter([data])

