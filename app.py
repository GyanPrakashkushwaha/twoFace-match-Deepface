
import streamlit as st
from PIL import Image
import os
from src.save_img import save_uploaded_img_face1 , save_uploaded_img_face2
from src.similarity import Similarity
from src.option_menus import option_menus
from src.pictures_mode import pictures_mode
from src.camera_mode import camera_mode
# from src.camera_mode import access_camera

st.set_page_config(page_title="Two-Face-Similarity", page_icon=":🙂:", layout="wide", initial_sidebar_state="expanded")

selected_mode , selected_model , selected_backend = option_menus()



st.title('Two Faces✌🏻(Similarity between two Faces)')

if selected_mode == 'Pictures':
    if pictures_mode() is not None:
        img1_path , img2_path = pictures_mode() 

        if st.button('Show Similarity'):
            try:
                sim = Similarity()

                similarity_score = sim.similarity(img1=img1_path,img2=img2_path,backend=selected_backend,model=selected_model)
                st.title(f'Similarity score: {similarity_score} %')
            except:
                st.write('Please select Different Backend Or Model')
else:
    if camera_mode() is not None:
        img1_path , img2_path = camera_mode()

        if st.button('Show Similarity'):
            try:
                sim = Similarity()

                similarity_score = sim.similarity(img1=img1_path,img2=img2_path,backend=selected_backend,model=selected_model)
                st.title(f'Similarity score: {similarity_score} %')
            except:
                st.write('Please select Different Backend Or Model')

                




    # st.camera_input(label='Smile Please'
    #     # access_camera()
    #     )
    # # access_camera()

    st.write('camera mode.')


