from typing import Union
import moondream as md
from PIL import Image

class MoondreamHelper:
    def __init__(self, api_key=None):
        self.model = md.vl(api_key=api_key)

    def _load_image(self, image: Union[Image.Image, str]):
        if isinstance(image, str):
            return Image.open(image)
        return None

    def caption(self, image: Union[Image.Image, str], length: str = "normal") -> str:
        caption = self.model.caption(image, length=length)
        return caption["caption"]

    def query(self, image: Union[Image.Image, str], question: str) -> str:
        query = self.model.query(image, question)
        return query["answer"]
    
    def detect(self, image: Union[Image.Image, str], object: str):
        coordinates = self.model.detect(image, object)
        return coordinates["objects"]