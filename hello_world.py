from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World - App Runner Test</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                text-align: center; 
                margin-top: 100px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            h1 { font-size: 3em; margin-bottom: 20px; }
            p { font-size: 1.5em; }
            .container { 
                background: rgba(255,255,255,0.1); 
                padding: 40px; 
                border-radius: 20px;
                backdrop-filter: blur(10px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Hello World!</h1>
            <p>If you can see this, App Runner deployment is working!</p>
            <p>✅ Python: Working</p>
            <p>✅ Flask: Working</p>
            <p>✅ App Runner: Working</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
