import streamlit as st
from PIL import Image
import os
from src.save_img import save_uploaded_img_face1 , save_uploaded_img_face2
from src.similarity import Similarity


def pictures_mode():
        
    col1 ,col2 = st.columns(2)
    with col1:
        img1 = st.file_uploader('Upload Image',key='image1')

    with col2:
        img2 = st.file_uploader('Upload New Image',key='image2')


    if img1 and img2 is not None:
        if save_uploaded_img_face1(img1) and save_uploaded_img_face2(img2):
            display_img1 = Image.open(img1)
            display_img2 = Image.open(img2)


            col3 , col4 = st.columns(2)
            with col3:
                st.image(image=display_img1,width=350,channels='BGR',caption='Your Image')
                # st.write(face_array1)

            with col4:
                st.image(image=display_img2,width=350,channels='BGR',caption='Your New Image')
                # st.write(face_array2)

            img1_path =os.path.join('images/uploaded_images/face1',img1.name)
            img2_path =os.path.join('images/uploaded_images/face2',img2.name)

        
            return img1_path , img2_path
        else:
            return None ,None

            # if st.button('Show Similarity'):
            #     try:
            #         sim = Similarity()

            #         similarity_score = sim.similarity(img1=img1_path,img2=img2_path,backend=selected_backend,model=selected_model)
            #         st.title(f'Similarity score: {similarity_score} %')
            #     except:
            #         st.write('Please select Different Backend Or Model')


                



