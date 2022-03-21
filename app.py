# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 17:23:50 2022

@author: shaik
"""

import numpy as np
import pickle
import streamlit as st



# Loading the saved model
loaded_model=pickle.load(open('trained.pkl','rb'))


# creating a function for prediction
def cancer_prediction(input_data):
    
    

    # values are in tuple ,will convert it into numpy arrays
    input_data_as_numpy_array=np.asarray(input_data)

    # reshape the numpy array as we are predicting one data array
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==2):
        return 'Breast Cancer is Malignant'
    else:
        return 'Breast Cancer is Benign'
    

def main():
    
    # title
    st.title("BREAST CANCER PREDICTION")
    
    # input data from user
    #radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst",
    #code-number 	ClumpThick 	Unicell 	Unicellshape 	Marg-ad 	Sin-Empi-cell-size 	Bare-Nucl 	Blnd-Chrom 	Nor-Nucl 	Mito 	class
    
    code_number =st.text_input('code-number ')
    ClumpThick=st.text_input('ClumpThick')
    Unicell =st.text_input('Unicell')
    Unicellshape=st.text_input('Unicellshape')
    Marg_ad=st.text_input('Marg-ad ')
    Sin_Empi_cell_size =st.text_input('Sin-Empi-cell-size')
    Bare_Nucl =st.text_input('Bare-Nucl')
    Blnd_Chrom =st.text_input('Blnd-Chrom ')
    Nor_Nucl=st.text_input('Nor-Nucl')
    Mito=st.text_input('Mito')
    
    
    
    # Prediction
    diagnosis=''
    
    # Button for prediction
    if st.button('Predict Breast Cancer'):
        diagnosis=cancer_prediction([code_number,ClumpThick,Unicell,Unicellshape,Marg_ad,Sin_Empi_cell_size,Bare_Nucl,Blnd_Chrom,Nor_Nucl,Mito ])
        
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
    