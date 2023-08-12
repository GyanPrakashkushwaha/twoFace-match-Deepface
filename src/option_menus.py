
from streamlit_option_menu import option_menu
import streamlit as st


def option_menus():

    selected_mode = option_menu(menu_title=None,
                            options=['Camera','Pictures'],
                            icons=['camera-fill','images'],
                            orientation='horizontal',
                            default_index=1,
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
        

    return selected_mode , selected_model , selected_backend
