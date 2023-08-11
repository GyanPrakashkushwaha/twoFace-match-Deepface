from deepface import DeepFace

class Similarity:
    def __init__(self) -> None:
        pass

    def similarity(self,img1,img2,backend,model):
        simi = DeepFace.verify(img1_path=img1,img2_path=img2,model_name=model,detector_backend=backend)
        simialrity = simi['distance']
        simialrity_in_percentage = round(100*(1-simialrity),ndigits=2)
        # round(100*(1- sim['distance']),ndigits=3)
        
        return simialrity_in_percentage
