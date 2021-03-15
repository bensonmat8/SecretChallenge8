from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Challenge1', methods=['GET', 'POST'])
def challenge1():
    columns = None
    if request.method == 'POST':
        uploaded_file = request.files['data_file']
        content = uploaded_file.read().split('\n')
        columns = [x for x in content[0].split('\t')]
    return render_template('challenge1.html', columns=columns)

@app.route('/Challenge2', methods=['GET', 'POST'])
def challenge2():
    return render_template('challenge2.html')

@app.route('/Challenge3', methods=['GET', 'POST'])
def challenge3():
    return render_template('challenge3.html')