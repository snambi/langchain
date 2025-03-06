import streamlit as st

from ollama_api import generate_restaurant_name

# def generate_restaurent_name(cuisine:str):
#     return {
#         'cuisine': "indian",
#         'menu_items': 'samosa, paneer tikka, idly, dosa'
#     }

st.title("Restaurant Name generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "American", "Mexican", "Arabic", "French", "Chinese"))

if cuisine:
    response = generate_restaurant_name(cuisine)
    st.header(response['cuisine'])
    items = response['menu_items'].split(",")

    st.write("**Menu Items**")
    for x in items:
        st.write("-", x)


