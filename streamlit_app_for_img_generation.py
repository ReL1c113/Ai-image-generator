# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:10:26 2024

@author: piyush.raj
"""

import streamlit as st
from image_generator_execution import img_generator

generator=img_generator()

st.title("AI Image Generator")

# Input field for the user's name
prompt = st.text_input("Enter your Prompt:")

# Check if the 'name' is submitted and store it in session state
if prompt:
    st.session_state["prompt"] = prompt
    
image_url = generator.flux_image_generator(prompt)

st.image(image_url, caption="This is an image from the web.", use_column_width=True)