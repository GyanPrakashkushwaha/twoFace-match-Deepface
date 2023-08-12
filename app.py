
import streamlit as st
from PIL import Image
import os
from src.save_img import save_uploaded_img_face1 , save_uploaded_img_face2
from src.similarity import Similarity
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Two-Face-Similarity", page_icon=":🙂:", layout="wide", initial_sidebar_state="expanded")

selected_mode = option_menu(menu_title=None,
                        options=['Camera','Pictures'],
                        icons=['camera-fill','images'],
                        orientation='horizontal',
                        menu_icon='airplane-engines-fill')


with st.sidebar:

    selected_model = option_menu(menu_title='SELECT MODEL',
                        options=['VGG-Face','FaceNet','Facenet512','OpenFace','DeepFace','DeepID','ArcFace','Dlib','SFace'],
                        # icons=['GlyphCraft', 'IconCraft', 'IconCraft', 'IconCraft', 'IconCraft', 'IconCraft', 'IconCraft', 'IconCraft', 'IconCraft'],
                        # orientation='horizontal',
                        menu_icon='airplane-engines-fill')

    selected_backend = option_menu(menu_title='SELECT BACKEND',
                      options=['opencv','ssd','dblib','mtcnn','retinaface','mediapipe'],
                    #   orientation='horizontal',
                      menu_icon='rocket-takeoff-fill')


st.title('Two Faces✌🏻(Similarity between two Faces)')
col1 ,col2 = st.columns(2)
with col1:
    img1 = st.file_uploader('Upload Image')

with col2:
    img2 = st.file_uploader('Upload New Image')



if img1 and img2 is not None:
    if save_uploaded_img_face1(img1) and save_uploaded_img_face2(img2):
        # face_array1 = detect_face(image_path=os.path.join('uploaded_images',img1.name))
        # face_array2 = detect_face(image_path=os.path.join('uploaded_images',img2.name))
        display_img1 = Image.open(img1)
        display_img2 = Image.open(img2)


        col3 , col4 = st.columns(2)
        with col3:
            st.image(image=display_img1,width=350,channels='BGR',caption='Your Image')
            # st.write(face_array1)

        with col4:
            st.image(image=display_img2,width=350,channels='BGR',caption='Your New Image')
            # st.write(face_array2)

        img1_path = image_path=os.path.join('images/uploaded_images/face1',img1.name)
        img2_path = image_path=os.path.join('images/uploaded_images/face2',img2.name)

        if st.button('Show Similarity'):
            try:
                sim = Similarity()

                similarity_score = sim.similarity(img1=img1_path,img2=img2_path,backend=selected_backend,model=selected_model)
                st.title(f'Similarity score: {similarity_score} %')
            except:
                st.write('Please select Different Backend Or Model')


       