import pandas as pd
from sklearn import linear_model
import tkinter as tk 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


df= pd.read_csv('C:\\Users\\Agnim S\\Desktop\\FINALSTUDENTDATA.csv')
X = df[['MSI','MSII','INTERNAL','EXTERNAL']].astype(int) # here we have 2 input variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['ENDSEM'].astype(int) # output variable (what we are trying to predict)

# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# tkinter GUI
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()

# with sklearn
Intercept_result = ('Intercept: ', regr.intercept_)
label_Intercept = tk.Label(root, text=Intercept_result, justify = 'center')
canvas1.create_window(260, 220, window=label_Intercept)

# with sklearn
Coefficients_result  = ('Coefficients: ', regr.coef_)
label_Coefficients = tk.Label(root, text=Coefficients_result, justify = 'center')
canvas1.create_window(260, 240, window=label_Coefficients)

# New_Interest_Rate label and input box
label1 = tk.Label(root, text='MS-I: ')
canvas1.create_window(100, 100, window=label1)

entry1 = tk.Entry (root) # create 1st entry box
canvas1.create_window(270, 100, window=entry1)

Intercept2_result = ('Intercept: ', regr.intercept_)
label2_Intercept = tk.Label(root, text=Intercept_result, justify = 'center')
canvas2.create_window(260, 220, window=label_Intercept)

# with sklearn
Coefficients2_result  = ('Coefficients: ', regr.coef_)
label2_Coefficients = tk.Label(root, text=Coefficients_result, justify = 'center')
canvas2.create_window(260, 240, window=label_Coefficients)

# New_Unemployment_Rate label and input box
label2 = tk.Label(root, text=' MS-II: ')
canvas2.create_window(120, 120, window=label2)

entry2 = tk.Entry (root) # create 2nd entry box
canvas2.create_window(270, 120, window=entry2)

label3 = tk.Label(root, text='INTERNAL: ')
canvas3.create_window(100, 100, window=label3)

entry3 = tk.Entry (root) # create 3rd entry box
canvas3.create_window(270, 100, window=entry3)

label4 = tk.Label(root, text='EXTERNAL: ')
canvas4.create_window(100, 100, window=label4)

entry1 = tk.Entry (root) # create 4th entry box
canvas1.create_window(270, 100, window=entry4)

def values(): 
    global MSI #our 1st input variable
    MSI = float(entry1.get()) 
    
    global MSII #our 2nd input variable
    MSII = float(entry2.get()) 

    global INTERNAL #our 3rd input variable
    INTERNAL = float(entry3.get()) 
    
    global EXTERNAL #our 3rd input variable
    EXTERNAL = float(entry4.get()) 

    Prediction_result  = ('END SEM MARKS : ', regr.predict([[MSI,MSII,INTERNAL,EXTERNAL]]))
    label_Prediction = tk.Label(root, text= Prediction_result, bg='orange')
    canvas1.create_window(260, 280, window=label_Prediction)
    
button1 = tk.Button (root, text='END SEM MARKS ',command=values, bg='orange') # button to call the 'values' command above 
canvas1.create_window(270, 150, window=button1)
 

root.mainloop()   