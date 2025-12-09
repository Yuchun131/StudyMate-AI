from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, StudyMate! The project is LIVE.'

if __name__ == '__main__':
    app.run(debug=True)