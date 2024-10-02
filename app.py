import streamlit as st
from utils import generate_caption

# Set the page configuration
st.set_page_config(
    page_title="Streamlit App",
    page_icon="🧊",
)

# set the title
st.title("Image Caption Generator")

file_=st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if file_ is not None:
    if st.button("Generate Caption"):
        response=generate_caption(file=file_)
        col1,col2=st.columns(2)
        with col1:
            st.image(file_,use_column_width=True,width=300)
            
        with col2:
            st.write(response[0]["generated_text"])