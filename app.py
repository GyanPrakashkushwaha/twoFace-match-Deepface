
import streamlit as st








st.set_page_config(page_title="Two-Face", page_icon=":😄:", layout="wide", initial_sidebar_state="expanded")


st.title('Two Faces✌🏻(Similarity between two Faces)')
col1 ,col2 = st.columns(2)
with col1:
    img1 = st.file_uploader('Upload Image')

with col2:
    img2 = st.file_uploader('Upload New Image')

if img1 and img2 is not None:
    if save_uploaded_img(img1) and save_uploaded_img(img2):
        face_array1 = detect_face(image_path=os.path.join('uploaded_images',img1.name))
        face_array2 = detect_face(image_path=os.path.join('uploaded_images',img2.name))
        display_img1 = Image.open(img1)
        display_img2 = Image.open(img2)


        col3 , col4 = st.columns(2)
        with col3:
            st.image(image=display_img1,width=350,channels='BGR',caption='Your Image')
            # st.write(face_array1)

        with col4:
            st.image(image=display_img2,width=350,channels='BGR',caption='Your New Image')
            # st.write(face_array2)

        rec = Recommend()
        pred1 , pred2 = rec.prediction(face_array1=face_array1,face_array2=face_array2)

        output = rec.similarity(result1=pred1,result2=pred2)
        st.markdown(f'> ## Both Faces Similarity score is :{round(100*(output[0][0]),ndigits=3)}%')
        
