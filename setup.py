from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/docs/list.html')
def list():
    return render_template('/docs/list.html')

@app.route('/docs/add.html')
def add():
    return render_template('/docs/add.html')

@app.route('/docs/random.html')
def random():
    return render_template('/docs/random.html')

if __name__ == '__main__':
    app.run()
