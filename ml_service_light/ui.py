import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

st.title("Iris classification model")

st.markdown("List iris characteristics:")
sepal_width = st.number_input(label="Sepal width", min_value=0, max_value=10, value=5)
sepal_height = st.number_input(label="Sepal height", min_value=0, max_value=10, value=5)
petal_width = st.number_input(label="Petal width", min_value=0, max_value=10, value=5)
petal_height = st.number_input(label="Petal height", min_value=0, max_value=10, value=5)

if st.button("Predict"):
    data = load_iris()
    X = data["data"]
    y = data["target"]

    model = LogisticRegression()
    model.fit(X, y)

    predict = model.predict([[sepal_width, sepal_height, petal_width, petal_height]])
    predict = data["target_names"][predict][0]

    st.success(f"This iris is {predict}.")
