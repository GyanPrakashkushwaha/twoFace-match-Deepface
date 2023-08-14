from deepface import DeepFace
import streamlit as st
import cv2
import numpy as np

def analyze_image(image):
    # Perform facial analysis using DeepFace
    result = DeepFace.analyze(image)
    return result

def main():
    st.title("Webcam Facial Analysis with DeepFace")
    
    # Create a video capture object
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        st.error("Failed to open webcam.")
        return
    
    stframe = st.empty()
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            st.error("Failed to capture frame from webcam.")
            break
        
        # Perform facial analysis
        result = analyze_image(frame)
        
        # Display the frame and analysis results
        stframe.image(frame, channels="BGR", caption="Webcam Feed")
        place_holder = st.empty()
        place_holder.text(result[0])
        place_holder = st.empty()
        st.write("Facial Analysis Results:")
        # st.write(result)
    
    cap.release()

if __name__ == "__main__":
    main()


