# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Bikram.Sahoo@Evalueserve.com 
"""
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
#from sklearn.externals import joblib 
import joblib
import joblib
  
# Load the model from the file 
Boston = joblib.load(r'C:\Users\Bikram.Sahoo\Documents\Tech_wed\boston-house-price-prediction--master\boston-house-price-prediction--master\boston.pkl')  
  
# Use the loaded model to make predictions 
#Boston.predict(X_test) 

def predict_price(LASAT,RM,INDUS,PTRATIO):
   
    prediction=Boston.predict([[LASAT,RM,INDUS,PTRATIO]])
    print(prediction)
    return prediction



def main():
    
    def add_bg_from_url():
        st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url("https://lc.zoocdn.com/9f2d741927ffa878efa9a4ffa181dfcb119f7fc3.jpg\");
                    background-attachment: fixed;
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

    add_bg_from_url() 

    html_temp = """
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;">Boston House Price Prediction ML App </h2>
    </div>
    
    <br>
    <br>
    """
    
    
    #st.markdown('<style>body{background-color:tomato;}</style>',unsafe_allow_html=True)
    st.markdown(html_temp,unsafe_allow_html=True)
    
    LASAT=st.number_input('lower status of the population in %')
    RM=st.number_input('Average number of rooms per dwelling')
    INDUS=st.number_input('Proportion of non-retail business acres per town')
    PTRATIO=st.number_input('Pupil-teacher ratio by town')
    result=''
    
    if st.button("Predict"):
        result=predict_price(LASAT,RM,INDUS,PTRATIO)  
        st.success('House price is: {} k$'.format(abs(result[0].round(2)))) 
       
    
    
    
    
    
    
if __name__=='__main__':
    main() 