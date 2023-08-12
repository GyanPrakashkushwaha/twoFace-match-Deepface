
import streamlit as st
from PIL import Image
import os
from src.save_img import save_uploaded_img_face1 , save_uploaded_img_face2

def camera_mode():
    col1 ,col2 = st.columns(2)
    with col1:

        img1 = st.camera_input('Smile Please',key='Hello')

    with col2:
        img2 = st.camera_input('Smile Please new',key='HII')


    if img1 and img2 is not None:
        if save_uploaded_img_face1(img1) and save_uploaded_img_face2(img2):

            img1_path =os.path.join('images/uploaded_images/face1',img1.name)
            img2_path =os.path.join('images/uploaded_images/face2',img2.name)

        
            return img1_path , img2_path
        else:
            return None ,None
        

