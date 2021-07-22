import base64
import os
from PIL import Image
from flask import (Flask, request, send_file)
import urllib
import cStringIO
import StringIO 
import re

app = Flask(__name__)
port = int(os.getenv("PORT", 18080))
defaultSizes = 1920, 1920

def getFileExt(url):
    rv = None
    m = re.match('^.+\.([^.]+)$', url)
    if m:
        rv = m.group(1)
    return rv

def getFileName(url):
    rv = None
    m = re.match('^.+/(.+?)\.[A-Za-z]{3,4}$', url)
    if m:
        rv = m.group(1)
    return rv

@app.route('/', methods = ['POST', 'GET'])
def thumb():
    w = request.args.get('w')
    h = request.args.get('h')
    if w is None:
        w = defaultSizes[0]

    if h is None:
        h = defaultSizes[1]
    
    size = int(w), int(h)

    urlBase64 = request.args.get('urlBase64')
    if urlBase64:
        url = base64.b64decode(urlBase64)
    else:
        url = request.args.get('url')

    if not url:
        return "Homepage"

    print("Processing URL \"%s\" now ..." % url)
    file = cStringIO.StringIO(urllib.urlopen(url).read())
    img = Image.open(file)
    img.thumbnail(size)
    img_io = StringIO.StringIO()
    img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True, debug=False)
