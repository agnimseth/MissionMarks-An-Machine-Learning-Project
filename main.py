from flask import Flask, render_template,request
app = Flask(__name__)
import pickle

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
        print(ABC)
        return render_template('show.html',MK=ABC) 
    return render_template('index.html')

@app.route('/Analysis')
def hello_world1():
    
    return render_template('analysis.html')
    


if __name__ == "__main__":
    app.run(debug=True)
