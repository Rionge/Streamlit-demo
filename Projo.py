# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:40:15 2023

@author: victor mburu ng'ang'
"""


import pickle
import streamlit as st

#load the saved model
loaded_model = pickle.load(open('C:/Users/Project/projo_0.sav','rb'))

#creating a function for prediction
#pass year as a parameteras we want to take year as an input

def prediction():
    if prediction[0] == 0:
        print('The model predicts that the new sample is of low quality.')
    else:
        print('The model predicts that the new sample is of high quality.')

    
    
def main():
    
    #giving the tittle for the web app
    st.title('Wine Quality')
    
    #getting the input variable
    
    default = st.number_input('Prediction on wine quality')
    
    #code from prediction
    
    #empty string for storing the whole result
    result = ''
    
    #creating a button
    if st.button('Final Prediction'):
        result = prediction(default) #allthe input data should be measured in the same order as needed by the model
        
    st.success(result)
    
#Run the main function
if __name__ =='__main__':
    main()
