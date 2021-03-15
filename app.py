from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.secret_key = b'This is a long test secret key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Challenge1', methods=['GET', 'POST'])
def challenge1():
    columns = None
    if request.method == 'POST':
        uploaded_file = request.files['data_file']
        try:
            content = uploaded_file.read().decode("utf-8").split('\n')
        except:
            flash('Invalid file given, please try again')
            return render_template('challenge1.html', columns=columns)
        columns = [x for x in content[0].split('\t')]
        if '7_2009' not in columns:
            flash("Column '7_2009' not found in the file, please try again.")
            render_template('challenge1.html', columns=columns)
    return render_template('challenge1.html', columns=columns)

@app.route('/Challenge2', methods=['GET', 'POST'])
def challenge2():
    return render_template('challenge2.html')

@app.route('/Challenge3', methods=['GET', 'POST'])
def challenge3():
    return render_template('challenge3.html')