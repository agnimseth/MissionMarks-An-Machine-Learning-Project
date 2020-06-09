from flask import Flask, render_template,request ,send_file
app = Flask(__name__)
import pickle
import pandas as pd
import plotly
import plotly.graph_objs as go
import json
import numpy as np
from io import BytesIO
from matplotlib import pyplot as plt
from  matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import jinja2
plt.style.use('ggplot')


app = Flask(__name__)
my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader("templates/"),
])
app.jinja_loader

file = open('model.pkl', 'rb')
clf  = pickle.load(file)
file.close()





@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        MSI=int(myDict['MSI'])
        MSII=int(myDict['MSII'])
        INTERNAL=int(myDict['INTERNAL'])
        EXTERNAL=int(myDict['EXTERNAL'])
        
        
        inputfeatures = [MSI, MSII, INTERNAL, EXTERNAL]
        ABC = clf.predict([inputfeatures])
        return render_template('show.html', MK = int(ABC)) 
    return render_template('index.html')

def create_plot():

    dataG = pd.read_csv('C:\\Users\\Agnim S\\Desktop\\FINALSTUDENTDATA.csv')
                         # creating a sample dataframe


    data = [
        go.Bar(
            x=dataG['MS-I'], # assign x as the dataframe column 'x'
            y=dataG['EXTERNAL']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/Analysis')
def hello_world1():
    data3 = pd.read_csv('C:\\Users\\Agnim S\\Desktop\\FINALSTUDENTDATA.csv')
    ana = data3.describe()
    data31 = pd.read_csv('C:\\Users\\Agnim S\\Desktop\\FINALSTUDENTDATA.csv')
    desc = data31["MS-I"].describe()
    aaa1=desc.to_frame()
    desc1 = data31["MS-II"].describe()
    aaa2=desc1.to_frame()
    desc2 = data31["INTERNAL"].describe()
    aaa3=desc2.to_frame()
    desc3 = data31["EXTERNAL"].describe()
    aaa4=desc3.to_frame()
    desc4 = data31["ENDSEM"].describe()
    aaa5=desc4.to_frame()
    print(data3.info())


    abb1 =data31.groupby(['MS-I', 'MS-II']).mean()
    abb3 = data31.groupby(['INTERNAL','EXTERNAL']).mean()

    abb2 = data31.groupby(['MS-I','MS-II','INTERNAL','EXTERNAL']).sum()
    abb4 = data31.groupby(['MS-I','MS-II','INTERNAL','EXTERNAL']).mean()
    
    return render_template('analysis.html', tables=[ana.to_html(classes='data', header="true")],tables1=[aaa1.to_html(classes='data', header="true")],tables2=[aaa2.to_html(classes='data', header="true")],tables3=[aaa3.to_html(classes='data', header="true")], tables4=[aaa4.to_html(classes='data', header="true")],tables5=[aaa5.to_html(classes='data', header="true")],tables6=[abb1.to_html(classes='data', header="true")],tables7=[abb2.to_html(classes='data', header="true")],tables8=[abb3.to_html(classes='data', header="true")],tables9=[abb4.to_html(classes='data', header="true")])
    
@app.route('/Visualisation')
def vis(): 
    bar = create_plot()
    return render_template('visual.html', plot=bar)

    

@app.route('/Dataset')
def analysis():
    data1=pd.read_csv('C:\\Users\\Agnim S\\Desktop\\FINALSTUDENTDATA.csv')
    return render_template('dataset.html',  tables=[data1.to_html(classes='data', header="true")]) 
    

@app.route('/vis556')
def vis556():
    fig, ax = plt.subplots()
    df=pd.read_csv('C:\\Users\\Agnim S\\Desktop\\FINALSTUDENTDATA.csv')
    P1 = df['MS-I'].head(20)
    P2 = df['MS-II'].head(20)
    P = df['ENDSEM'].head(20)

    plt.plot(P1,P,color ="blue")
    plt.plot(P2,P,color = "orange")
    plt.xlabel('END SEM MARKS TOP 20')
    plt.ylabel('MS-I and MS-II')

    plt.title('MS Relation With EndSem marks')
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    im = send_file(img, mimetype='image/png')
    return render_template('vipic.html')


if __name__ == "__main__":
    app.run(debug=True)