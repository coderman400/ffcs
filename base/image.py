import cv2
import numpy as np


class SlotExtraction:
    def __init__(self,image_path):
        self.image = cv2.imread(image_path)


    def pre
