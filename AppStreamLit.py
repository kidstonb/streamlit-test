import streamlit as st
import pandas as pd
import pickle
# from pathlib import Path

# Load model file
# filename = Path('LogRDummyModel.pkl')
model = pickle.load(open('LogRDummyModel.pkl', 'rb'))

def predict(feature1, feature2, feature3):
    # code insurance to limit responses to within data range
    # Also to scale input appropriately 
    
    input = pd.DataFrame([[feature1, feature2, feature3]],columns=['feature1','feature2','feature3'])
    prediction = model.predict(input)
    return prediction

st.title('Wine Quality Prediction')
st.image('https://images.unsplash.com/photo-1585553616435-2dc0a54e271d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8d2luZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60')
st.header('Enter wine chemistry below')

# does value = 1.0 scale it?
feature1 = st.number_input('feature1', min_value = 0.0, max_value = 5.0, value=1.0)
feature2 = st.number_input('feature2', min_value = 0.0, max_value = 5.0, value=1.0)
feature3 = st.number_input('feature3', min_value = 0.0, max_value = 5.0, value=1.0)
colour = st.selectbox('Red or White:', ['Red','White'])

if st.button('Predict Quality'):
    quality = predict(feature1, feature2, feature3)
    st.success(f'The predicted wine quality is {quality}')