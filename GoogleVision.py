import io
import os
from google.cloud import vision
from google.cloud.vision import types
from google.cloud.vision import type
client = vision.ImageAnnotatorClient()
# we would have to change the bottom part we could have some sort of input shit
file_name = os.path.join(
    os.path.dirname(__file__),
    'car.jpg')

with io.open(file_name,"rb") as image_file:
        content = image_file.read()

image = type.Image(content=content)

response = client.label_detection(image=image)

labels = response.label_annotations

print("labels: ")
    print((label.description))

