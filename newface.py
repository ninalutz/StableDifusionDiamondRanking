import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
import os
import csv
import numpy as np

input_folder_name = "GStudy/Gender/A man/Europe/France man/"
category = "france_man"

centers = []

# For static images:
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

for i in range(1, 51):
  file = input_folder_name + str(i) + ".png"
  with mp_face_mesh.FaceMesh(static_image_mode=True, min_detection_confidence=0.5) as face_mesh:
    image = cv2.imread(file)
    # Convert the BGR image to RGB before processing.
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # Print and draw face mesh landmarks on the image.
    if not results.multi_face_landmarks:
      centers.append([256, 256])
      continue
    annotated_image = image.copy()
    for face_landmarks in results.multi_face_landmarks:
      # print('face_landmarks:', face_landmarks)
      mp_drawing.draw_landmarks(
          image=annotated_image,
          landmark_list=face_landmarks,
          connections=mp.solutions.face_mesh.FACEMESH_TESSELATION,
          landmark_drawing_spec=drawing_spec,
          connection_drawing_spec=drawing_spec)
    count = 0 
    for face in results.multi_face_landmarks:
        for landmark in face.landmark:
            x = landmark.x
            y = landmark.y
            count += 1
            shape = image.shape 
            relative_x = int(x * shape[1])
            relative_y = int(y * shape[0])
            if count == 2: 
              # print(i)
              # print(relative_x, relative_y)
              centers.append([relative_x, relative_y])
              # print(len(centers))

with open('centers.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for row in centers:
      spamwriter.writerow(row)

image_data = []


#get ALL the images into an image object 
for i in range(1, 51):
  file = input_folder_name + str(i) + ".png"
  cv_image = cv2.imread(file)
  ht, wd, cc= cv_image.shape

  ww = wd*2 
  hh = ht*2
  color = (255,255,255)
  result = np.full((hh,ww,cc), color, dtype=np.uint8)

  # print(len(centers))
  # set offsets for top left corner
  xx = int(ww/2) - centers[i-1][0]
  yy = int(hh/2) - centers[i-1][1]

  # copy img image into center of result image
  result[yy:yy+ht, xx:xx+wd] = cv_image

  cv2.imwrite('res_' + str(i) + ".png", result)  


  image_data.append(result)

# Initialize the average image with the first image in the list
avg_image = image_data[0]

# Loop through each image in the list
for i in range(len(image_data)):
    # Skip the first image (i == 0) as it is already set as the average image
    if i == 0:
        pass
    else:
        # Calculate alpha and beta for weighted addition
        alpha = 1.0 / (i + 1)
        beta = 1.0 - alpha

        # Update the average image using weighted addition
        avg_image = cv2.addWeighted(image_data[i], alpha, avg_image, beta, 0.0)

# Save the averaged image to a PNG file
cv2.imwrite("average_" + category + '.png', avg_image)


