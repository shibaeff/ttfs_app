from datetime import datetime
from io import StringIO
from PIL import Image

def application(environ, start_response):
    """Simplest possible application object"""
    
    status = "200 OK"
    root = "/home/paavo/Рабочий стол/ttffs_app"
    path = (root + environ["PATH_INFO"])
    
    file = open(path, "rb").read()
    
    print(path)
    response_headers = [
        ('Content-type', 'text/html'),
        ('Content-Length', str(len(file)))
    ]
    return [file]