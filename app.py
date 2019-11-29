import urllib
import draw as draw

from flask import Flask, request
#import draw

app = Flask(__name__, static_url_path='')


@app.route('/')
def hello_world():
    return app.send_static_file('home.html')


@app.route('/alex')
def alex():
    return 'I love you'


@app.route('/sendimg/', methods=['POST'])
def sendimg():
    print(request.data.decode("UTF-8"))

    data = request.data.decode("UTF-8")
    response = urllib.request.urlopen(data)
    with open('tree.jpg', 'wb') as f:
        f.write(response.file.read())
    draw.generate_path()
    return '{"status": "running"}'



if __name__ == '__main__':
    app.run()
