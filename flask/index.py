from flask import Flask, url_for, request
import os
app = Flask(__name__)
host='192.168.0.111'
os.chdir('flask/static/vid')

@app.route("/")
def index():
    
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Page Title</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
        <script src='main.js'></script>
    </head>
    <body>
        '''+ ''.join([f'<a href="/file/{i}">{i}</a><br/>' for i in os.listdir() if '.mp4' in i]) +'''
    </body>
    </html>
    '''

@app.route("/file/<name>")
def file(name):
    return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Page Title</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
    <script src='main.js'></script>
    <link rel="stylesheet" 
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
    crossorigin="anonymous">
</head>
<body>
    <center>
        <div style="width: 700px; float: center;">
            <div class="alert alert-primary" role="alert" style="height: 560px; padding: 20px;">
                <center>
                    <video controls="controls">
                        <source src="{url_for('static', filename='vid/'+name)}" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
                    </video>
                </center>
                <a href="{url_for('static', filename='vid/'+name)}" download><button type="button" class="btn btn-success" style="float: left;">Скачать</button></a>
                <a href="http://{host}:8000"><button type="button" class="btn btn-primary" style="float: right;">Главная</button></a>
            </div>
        </div>
    </center>
</body>
</html>
    '''


if __name__ == "__main__":
    app.run(host=host, port=8000)
