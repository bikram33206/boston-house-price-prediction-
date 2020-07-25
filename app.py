# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from sklearn.externals import joblib 
  
# Load the model from the file 
Boston = joblib.load('boston.pkl')  
  
# Use the loaded model to make predictions 
#Boston.predict(X_test) 

def predict_price(LASAT,RM,INDUS,PTRATIO):
   
    prediction=Boston.predict([[LASAT,RM,INDUS,PTRATIO]])
    print(prediction)
    return prediction



def main():
    
   
    html_temp = """
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;">Boston House Price Prediction ML App </h2>
    </div>
    
    <br>
    <br>
    """
    
    
    st.markdown('<style>body{background-color:tomato;}</style>',unsafe_allow_html=True)
    st.markdown(html_temp,unsafe_allow_html=True)
    
    LASAT=st.number_input('lower status of the population in %')
    RM=st.number_input('Average number of rooms per dwelling')
    INDUS=st.number_input('Proportion of non-retail business acres per town')
    PTRATIO=st.number_input('Pupil-teacher ratio by town')
    result=''
    
    if st.button("Predict"):
        result=predict_price(LASAT,RM,INDUS,PTRATIO)  
        
    st.success('House price is: {} k$'.format(result[0]))    
    
    
    
    
    
    
if __name__=='__main__':
    main() 