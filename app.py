from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    value = int(request.form['value'])
    if 1 <= value <= 100:
        return render_template('welcome.html')
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
