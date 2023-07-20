import json
import math
import numpy as np
from matplotlib import pyplot as plt



im = plt.imread('./out/test/scene-0029_empty_720.png')


# plt.imshow(im)
# plt.show()


nPix = len(im)


y_normal = []

for y in reversed(range(nPix)) :
    # print(len(im[y]))
    # print(im[y])

    x_normal =[]

    for x in im[y]:
        # print(x)
        if (all(xval ==1  for xval in x)):
            # print('w')
            x_normal.append(1) # white =1 = violate
        else:
            # print('b')
            x_normal.append(0)

    y_normal.append(x_normal)


# for y in  y_normal:
#     print(x)



# plot image with correct axis
im = plt.imshow(np.flipud(plt.imread('./out/test/scene-0029_empty_720.png')), origin='lower', extent=[0,720,0,720],aspect='1')


# for y_enu, y in enumerate(y_normal):
#     # y0, y1 ...
#     for x_enu, x in enumerate(y):

#         print(y)

#         print(str(x_enu) + ' ' + str(y_enu))
#         # plt.plot(x, y, marker="o", markersize=5, markerfacecolor="red")



for x in range(720):
    for y in range(400,405):
        print(y_normal[y][x])
        if y_normal[y][x] == 1:
            plt.plot(x, y, marker="o", markersize=5, markerfacecolor="red")



plt.show()


