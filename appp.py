import streamlit as st
import numpy as np
import pickle
with open('Save.pkl','rb') as file:
    model=pickle.load(file)
st.title("Heart beats and Oxygen saturation")
st.write("Fill the following Information to get the prediction")

age=st.number_input("Enter the age", value=0.0)
Gender=st.selectbox("Select the Gender", ['Male','Female'])
heart=st.number_input("Enter the heart rate", value=0.0)
Resp=st.number_input("Enter Respiratory rate", value=0.0)
Temp=st.number_input("Enter the body temperature in Celcius", value=0.0)
oxy=st.number_input("Enter Oxygen Saturation", value=0.0)
Syst=st.number_input("Enter the Systolic Blood Pressure", value=0.0)
Dias=st.number_input("Enter the Diastolic Blood Pressure", value=0.0)
HRV=st.number_input("Enter the Derived HRV", value=0.0)
BMI=st.number_input("Enter the BMI", value=0.0)
MAP=st.number_input("Enter The Derived MAP")
val=0
if Gender=="Female":
    val=0
else:
    val=1
if st.button("Predict"):
    input_=np.array([[age,val,heart,Resp,Temp,oxy,Syst,Dias,HRV,BMI,MAP]])
    Pred=model.predict(input_)
    st.success(Pred[0])