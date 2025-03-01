import cv2
import numpy as np

input_folder_name = "GStudy/Person/"

file = input_folder_name + str(1) + ".png"
# read image
img = cv2.imread(file)
ht, wd, cc= img.shape

#TODO -- calculate the offset of the images to overlay onto each other 
## Offset from center is going to be the width -- 512px 
# create new image of desired size and color (white) for padding
ww = wd*2 
hh = ht*2
color = (255,255,255)
result = np.full((hh,ww,cc), color, dtype=np.uint8)

# set offsets for top left corner
xx = int(ww/2) - 187
yy = int(hh/2) - 214

# copy img image into center of result image
result[yy:yy+ht, xx:xx+wd] = img

# view result
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save result
cv2.imwrite("numbers_inserted.jpg", result)
