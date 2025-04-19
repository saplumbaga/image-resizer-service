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
defaultSizes = 960, 960

@app.route('/', methods=['POST', 'GET'])
def thumb():

    expected_token = os.environ.get('AUTH_TOKEN')
    auth_header = request.headers.get('Authorization')
    if auth_header != 'Bearer {}'.format(expected_token):
        return "Unauthorized", 401
    
    w = request.args.get('w')
    h = request.args.get('h')
    if w is None:
        w = defaultSizes[0]

    if h is None:
        h = defaultSizes[1]

    size = int(w), int(h)

    url64 = request.args.get('url64')
    if url64:
        url = base64.b64decode(url64)
    else:
        url = request.args.get('url')

    print("Processing URL \"%s\" now ..." % url)

    if url:
        file = cStringIO.StringIO(urllib.urlopen(url).read())
        img = Image.open(file)
        img.thumbnail(size)
    else:
        bg = request.args.get('bg')
        if not bg:
            bg = 0
        if len(bg) != 3 and len(bg) != 6:
            return "BAD REQUEST", 400
        
        img = Image.new("RGB", size, '#' + bg)

    img_io = StringIO.StringIO()

    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True, debug=False)
