
import streamlit as st
import numpy as np
import pickle

#Load the trained model
model = pickle.load(open('ckd_model.pkl', 'rb'))

st.title("Chronic Kidney Disease Prediction App")
st.markdown("Enter the patient information to predict the risk of CKD.")

st.sidebar.header("Patient Information")

def get_input():
  age = st.sidebar.slider("Age", 1, 100, 45)
  bp = st.sidebar.slider("Blood Pressure", 50, 200, 80)
  bgr = st.sidebar.slider("Blood Glucose Random", 70, 500, 140)
  bu = st.sidebar.slider("Blood Urea", 1, 300, 40)
  sc = st.sidebar.slider("Serum Creatine", 0.0, 15,0, 1.2)
  hemo = st.sidebar.slider("Hemoglobin", 3.0, 18.0, 12.0)
  pcv = st.sidebar.slider("Packed Cell Volume", 10, 60, 40)
  wc = st.sidebar.slider("White Blood Cell Count", 1000, 3000, 8000)
  rc = st.sidebar.slider("Red Blood Cell Count", 2.0, 8.0, 5.0)

  data = np.array([[age, bp, bgr, bu, sc, hemo, pcv, wc, rc]])
  return data

  input_data = get_input()

  if st.button("Predict CKD Risk"):
    result = model.predict(input_data)
    st.subheader("Prediction Result:")
    st.success("CKD Detected!"" if result[0]  == 1 else"No CKD Detected")