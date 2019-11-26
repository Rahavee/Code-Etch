import urllib

from flask import Flask, request
#import draw

app = Flask(__name__, static_url_path='')


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


@app.route('/run')
def run():
    print("I am inside here")
    return '{"status": "running"}'


@app.route('/alex')
def alex():
    return 'I love you'

@app.route('/fick')
def fick():
    return '{"status": "running"}'


@app.route('/sendimg/', methods=['POST'])
def sendimg():
    print(request.data.decode("UTF-8"))

    data = request.data.decode("UTF-8")
    response = urllib.request.urlopen(data)
    with open('tree.jpg', 'wb') as f:
        f.write(response.file.read())
    return '{"status": "running"}'


if __name__ == '__main__':
    app.hello_world()
