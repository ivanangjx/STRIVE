import cv2
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
import numpy as np
from matplotlib.patches import Circle


map_ori = cv2.imread('/home/ivan/STRIVE/server_out/adv_gen_rule_based_out_VAL/viz_results/adv_sol_success/scene-0015/scene-0015_before_vid_000/frame0000.png')

map_ori = cv2.cvtColor(map_ori, cv2.COLOR_BGR2RGB)

# plt.imshow(map_ori, origin='lower')
plt.imshow(map_ori)
plt.show()

# HSV input color range to segregate
color_range_low  = (0, 0, 253)
color_range_high = (0, 0, 255)


# # plot color chosen -----------------------------------------------------------
# lo_square = np.full((10, 10, 3), color_range_low, dtype=np.uint8) / 255.0
# do_square = np.full((10, 10, 3), color_range_high, dtype=np.uint8) / 255.0

# # plt.subplot(1, 2, 1)
# # plt.imshow(hsv_to_rgb(do_square))
# # plt.subplot(1, 2, 2)
# # plt.imshow(hsv_to_rgb(lo_square))
# # plt.show()
# #------------------------------------------------------------------------------


# get Hue, Saturation, and Value of image
hsv_map_ori = cv2.cvtColor(map_ori, cv2.COLOR_RGB2HSV)

mask = cv2.inRange(hsv_map_ori, color_range_low, color_range_high)

result = cv2.bitwise_and(map_ori, map_ori, mask=mask)

# plt.subplot(1, 2, 1)
# plt.imshow(mask, cmap="gray")
# plt.subplot(1, 2, 2)
# plt.imshow(result)
# plt.show()

# plt.imshow(result)
# plt.show()


cv2.imwrite('./out/EMPTY_MAPS_TEST/scene_0005_001_BW.png', result)

# #-------------------------------------------------



# print(result[415][451][0])
# print(result[60][800][0])


with np.printoptions(threshold=np.inf):
    print(result[800])


# x_list = []

# for x in range(len(thresh1)):
# 	y_list = []
# 	for y in range(len(thresh1[0])):
		
# 		if (thresh1[x][y][0] == 0):
# 			y_list.append(0)
# 		else:
# 			y_list.append(1)
# 			# print(y)

# 	x_list.append(y_list)		

# print(x_list)



x = [0]
y = [500]
# plt.xlim(0, 5)
# plt.ylim(0, 5)
# plt.grid()

plt.plot(x, y, marker="o", markersize=5, markerfacecolor="red")







plt.imshow(result)
plt.show()













# # reading image
# img = cv2.imread('./out/EMPTY_MAPS_TEST/scene_0005_001_BW.png')

# plt.imshow(img)
# plt.show()
  
# # converting image into grayscale image
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# plt.imshow(gray)
# plt.title('grey')
# plt.show()
  
# # setting threshold of gray image
# _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


# plt.imshow(threshold)
# plt.title('thres')
# plt.show()
  




# cont = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# output = np.zeros(gray.shape, dtype=np.uint8)
# cv2.drawContours(output, cont[0], -1, (255, 255, 255))

# plt.imshow(output)
# plt.show()

# # removing boundary
# boundary = 255*np.ones(gray.shape, dtype=np.uint8)
# boundary[1:boundary.shape[0]-1, 1:boundary.shape[1]-1] = 0

# toremove = output & boundary
# output = output ^ toremove


# plt.imshow(output)
# plt.show()


# point1 = [100, 200]
# point2 = [300, 400]
# x_values = [point1[0], point2[0]]
# y_values = [point1[1], point2[1]]
# plt.plot(x_values, y_values, 'bo', linestyle="--")
# plt.imshow(output)

# plt.show()