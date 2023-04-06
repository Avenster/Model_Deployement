import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title('What is the type IRIS? :blossom:')

sepal_length = st.slider("Sepal Length ",0.1,5.8)
sepal_width = st.slider("Sepal Width ",0.1,5.8)
petal_length = st.slider("Petal Length ",0.1,5.8)
petal_width = st.slider("Petal Width ",0.1,5.8)


def predict():
    float_features = [float(x) for x in [sepal_length, sepal_width, petal_length, petal_width]]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    label = prediction[0]
    
    print(type(label))
    print(label)

    st.success('The Flower is : ' + str(label) + ' :thumbsup:')
    
trigger = st.button('Predict', on_click=predict)

