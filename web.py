from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():

    return '<h3>Hey, we have Flask in a Docker container!</h3>'
    

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
