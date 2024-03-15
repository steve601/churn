import numpy as np 
import pickle

from flask import Flask,request,render_template

app = Flask(__name__)
model = pickle.load(open('churn.pkl','rb'))

@app.route('/')
def home():
    return render_template('churn.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    d1 = request.form['CreditScore']
    d2 = request.form['Geography']
    d3 = request.form['Gender']
    d4 = request.form['Age']
    d5 = request.form['Tenure']
    d6 = float(request.form['Balance'])
    d7 = request.form['NumOfProducts']
    d8 = request.form['HasCrCard']
    d9 = request.form['IsActiveMember']
    d10 = float(request.form['EstimatedSalary'])
    
    if d2 == 'Spain':
        d2 = 0
    if d2 == 'Germany':
        d2 = 1
    if d2 == 'France':
        d2 = 2
        
    if d3 == 'Male':
        d3 = 1
    if d3 == 'Female':
        d3 = 0
        
    arr = np.array([[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]])
    output = model.predict(arr)
    if output == 1:
        text = 'Customer is likely to leave.'
    else:
        text = 'Customer is likely to stay'
        
    return render_template('churn.html',pred_text = text)

if __name__ == '__main__':
    app.run(debug=True)