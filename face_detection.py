# -*- coding: utf-8 -*-
"""face_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XLanmbA2-pJx2MnFwDDk4e6lh8Qrl401
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install mtcnn

import numpy as np
import cv2
from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle
# from matplotlib.patches import Circle

image = cv2.imread('/content/photo_2023-10-23_15-49-59.jpg')
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)

mtcnn = MTCNN()
detected = mtcnn.detect_faces(rgb_image)
print(detected)
print(f"box : {detected[0]['box']}")
print(f"confidence : {detected[0]['confidence']}")
print(f"keypoints : {detected[0]['keypoints']}")

box = detected[0]['box']
confidence = detected[0]['confidence']
keypoints = detected[0]['keypoints']

x, y, width, height = box
plt.imshow(rgb_image)
# create the shape
rect = plt.Rectangle((x, y), width, height, fill=False, color='green')
# get the context for drawing boxes
ax = plt.gca()
# draw the box
ax.add_patch(rect)
# show the plot
plt.show()

plt.imshow(rgb_image)
# create the shape
rect = plt.Rectangle((x, y), width, height, fill=False, color='green')
# get the context for drawing boxes
ax = plt.gca()
# draw the box
ax.add_patch(rect)

for key, value in keypoints.items():
  # create and draw dot
  dot = plt.Circle(value, radius=3, color='orange')
  ax.add_patch(dot)

text = f"{confidence:.2f}"
font = {'family': 'serif', 'color':  'green', 'size': 12}
plt.text(x, y-15, text, fontdict=font, ha='left')
# show the plot
plt.show()