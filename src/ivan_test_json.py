import json
import math
import numpy as np
from matplotlib import pyplot as plt

with open('./out/test/scene-0029_safe.json', 'r') as f:
    data = json.load(f)



# print(data['1'])


# for indexes in data:
#     for coor in data[indexes]:
#         print(coor)
#     print("")


    # for traj in indexes:
    #     print(data[indexes][traj])




for indexes in data:
    if indexes == '0':
        x_list = []
        y_list = []
        for coor in data[indexes]:
            x = coor[0]
            y = coor[1]
            theta = math.atan2(coor[3], coor[2])
            print(str(x) + '   ' + str(y))

            x_list.append(x)
            y_list.append(y)
        plt.plot(x_list,y_list,'o')


im = plt.imread('./out/test/scene-0029_empty.png')
# fig, ax = plt.subplots()
# im = ax.imshow(im)
plt.imshow(im)



# plt.xlim([0, 720])
# plt.ylim([0, 720])
plt.show()