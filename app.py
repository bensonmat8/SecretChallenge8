from benford import benford_test
from flask import Flask, flash, render_template, request
import json
import plotly.express as px
from plotly.utils import PlotlyJSONEncoder

app = Flask(__name__)
with open('secretkey.txt','r') as secret:
    app.secret_key = secret.read()

@app.route('/Home')
@app.route('/')
def home():
    return render_template('home.html')

def graph_plot(data_count):
    '''
    Takes the data and returns plotly plot in JSON
    '''
    total = sum(data_count)
    data_count = [round(x/total*100, 1) for x in data_count]
    x = [x for x in range(1,10)]
    benford = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
    fig = px.line(x=x, y=benford)
    fig.data[0].name = "Benford Line"
    fig.add_bar(x=x, y=data_count, name='Observed Data')
    fig.update_layout(title="Benford's Test",
                    xaxis_title='Digits',
                    yaxis_title='Frequency (%)')
    graphJSON = json.dumps(fig, cls=PlotlyJSONEncoder)
    return graphJSON


@app.route('/Challenge1', methods=['GET', 'POST'])
def challenge1():
    '''
    Takes the flat file provided from the frontend page and
    runs the algorithm to check for benford_test and 
    displays the result and plot
    '''
    result = None
    plot = None
    if request.method == 'POST':
        uploaded_file = request.files['data_file']
        column_name = request.form.get('column_name')
        if uploaded_file.filename == '':
            flash('No File Given')
            return render_template('challenge1.html', result=result
            , plot=plot)
        if column_name == '':
            column_name = '7_2009'
        
        try:
            content = uploaded_file.read().decode("utf-8").split('\n')
        except:
            flash('Invalid file given, please try again')
            return render_template('challenge1.html', columns=columns)
        columns = [x for x in content[0].split('\t')]
        columns = columns + [x for x in content[0].split(',')]
        if column_name not in columns:
            flash(f"Column '{column_name}' not found in the file, please try again.")
            return render_template('challenge1.html', result=result
            , plot=plot)
        try:
            result, data_count = benford_test(content, column_name)
            plot =  graph_plot(data_count)
        except:
            flash('Invalid file/column name given, please try again')
            return render_template('challenge1.html', result=result
            , plot=plot)
    return render_template('challenge1.html', result=result
            , plot=plot)

@app.route('/Challenge1#', methods=['GET', 'POST'])
def challenge1_():
    '''
    This is similar to challenge1 as above, but
    are for users who don't have the data so
    it will use the data saved on static folder
    '''
    result=None
    plot = None
    with open('./static/census_2009b.txt','r') as file:
        content = file.read().split('\n')
    result, data_count = benford_test(content)
    plot =  graph_plot(data_count)
    return render_template('challenge1.html', result=result
            , plot=plot)

@app.route('/Challenge2', methods=['GET', 'POST'])
def challenge2():
    '''
    Displays the widgets solution 
    '''
    return render_template('challenge2.html')

@app.route('/Challenge3', methods=['GET', 'POST'])
def challenge3():
    '''
    Displays the error review solution
    '''
    return render_template('challenge3.html')