from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from cdmn.API import DMN
import time
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")

app = Flask(__name__)
path = 'BMILevel.dmn'
spec = DMN(path,auto_propagate=True)


# start an app route
@app.route('/')
# declare function
def main():
    return render_template('app.html')
    
    
# form submission route
@app.route('/predict', methods=["POST"])
def predict():
    if request.method == 'POST':
        resp = request.form
        # start pulling data from input

        Weight = resp.get('weight')
        hight = resp.get('hight')
        sex = resp.get('sex')
        waist = resp.get('waist')
        #peration = request.form.get('operation')
        weigth = float(Weight)
        hight = float(hight)
        sex = str(sex)
        sex = sex.title()
        waist = float(waist)
        
        # set value for DMN
        spec.set_value('weight', weigth)
        spec.set_value('length', hight)
        spec.set_value('sex', sex)
        spec.set_value('waist', waist)
        
        bmi = spec.value_of('bmi')
        bmilevel = spec.value_of('BMILevel')
        riskLevel = spec.value_of('riskLevel')
        
        return render_template('app.html', BMI=bmi, BMI_Level=bmilevel, Risk_Level=riskLevel )
                
        
        


if __name__ == '__main__':
    app.run(debug=True)