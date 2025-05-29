from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destino/<nombre>')
def infoTuris(nombre=None):
    return render_template('infoTuris.html')

if __name__ == '__main__':
    app.run(debug=True)