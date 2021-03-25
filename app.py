from benford import benford_test
from flask import Flask, flash, render_template, request
import json
import plotly.express as px
from plotly.utils import PlotlyJSONEncoder

app = Flask(__name__)
app.secret_key = b'This is a long test secret key'

@app.route('/')
def home():
    return render_template('home.html')

def graph_plot(data_count):
    total = sum(data_count)
    data_count = [round(x/total*100, 1) for x in data_count]
    x = [x for x in range(1,10)]
    benford = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
    fig = px.line(x=x, y=benford, labels="Benford Line")
    fig.add_bar(x=x, y=data_count, name='Observed Data')
    fig.update_layout(title="Benford's Test",
                    xaxis_title='Digits',
                    yaxis_title='Frequency (%)')
    graphJSON = json.dumps(fig, cls=PlotlyJSONEncoder)
    return graphJSON


@app.route('/Challenge1', methods=['GET', 'POST'])
def challenge1():
    result = None
    plot = None
    if request.method == 'POST':
        uploaded_file = request.files['data_file']
        try:
            content = uploaded_file.read().decode("utf-8").split('\n')
        except:
            flash('Invalid file given, please try again')
            return render_template('challenge1.html', columns=columns)
        columns = [x for x in content[0].split('\t')]
        columns = columns + [x for x in content[0].split(',')]
        if '7_2009' not in columns:
            flash("Column '7_2009' not found in the file, please try again.")
            render_template('challenge1.html', columns=columns)
        result, data_count = benford_test(content)
        plot =  graph_plot(data_count)
    return render_template('challenge1.html', result=result
            , plot=plot)

@app.route('/Challenge2', methods=['GET', 'POST'])
def challenge2():
    return render_template('challenge2.html')

@app.route('/Challenge3', methods=['GET', 'POST'])
def challenge3():
    return render_template('challenge3.html')