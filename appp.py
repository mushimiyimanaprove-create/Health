import streamlit as st
import numpy as np
import pickle
with open('Save.pkl','rb') as file:
    model=pickle.load(file)
st.title("Heart beats and Oxygen saturation")
st.write("Fill the following Information to get the prediction")

age=st.number_input("Enter the age")
Gender=st.selectbox("Select the Gender", ['Male','Female'])
heart=st.number_input("Enter the heart rate")
Resp=st.number_input("Enter Respiratory rate")
Temp=st.number_input("Enter the body temperature in Celcius")
oxy=st.number_input("Enter Oxygen Saturation")
Syst=st.number_input("Enter the Systolic Blood Pressure")
Dias=st.number_input("Enter the Diastolic Blood Pressure")
HRV=st.number_input("Enter the Derived HRV")
BMI=st.number_input("Enter the BMI")
MAP=st.number_input("Enter The Derived MAP")
val=0
if Gender=="Female":
    val=0
else:
    val=1
if st.button("Predict"):
    input_=np.array([[age,val,heart,Resp,Temp,oxy,Syst,Dias,HRV,BMI,MAP]])
    Pred=model.predict(input_)
    if Pred[0]==0:
        st.success("Patient has High Risk")
    else:
        st.success("Patient has Low Risk")
