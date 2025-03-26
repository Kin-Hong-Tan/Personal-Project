import streamlit as st
import requests

st.title("🛍️ Product Recommender")

user_id = st.number_input("Enter User ID:", min_value=1, max_value=1000, step=1)

if st.button("Get Recommendations"):
    response = requests.get(f"http://localhost:8000/recommend/{user_id}")
    recommendations = response.json().get('recommendations', [])
    
    st.write("Recommended Products:")
    for product in recommendations:
        st.write(f"- {product}")