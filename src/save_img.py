
import os

def save_uploaded_img_face1(image):
    try:
        with open(os.path.join('images/uploaded_images/face1',image.name),'wb') as file_:
            file_.write(image.getbuffer())
        return True 
    except:
        return False


def save_uploaded_img_face2(image):
    try:
        with open(os.path.join('images/uploaded_images/face2',image.name),'wb') as file_:
            file_.write(image.getbuffer())
        return True
    except:
        return False
