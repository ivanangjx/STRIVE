import json
import math
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.transforms import Affine2D

with open('./server_out/strive-scenario-replay-adv-sucess-data/scene_0005_001/scene_0005_001_safe.json', 'r') as f:
    data = json.load(f)



def plot_point(point, angle, length):

    x, y = point

    # find the end point
    endy = y + length * math.sin((angle))
    endx = x + length * math.cos((angle))

    print(endy)
    print(endx)

    plt.plot([x, endx], [y, endy])


print(data['lw'][0])

l = data['lw'][0][0]
w = data['lw'][0][1]


# for indexes in data:
#     for coor in data[indexes]:
#         print(coor)
#     print("")


    # for traj in indexes:
    #     print(data[indexes][traj])

fig = plt.figure()
ax = fig.add_subplot(111)


for indexes in data:
    print(indexes)

for indexes in data:
    if indexes == '0':
        x_list = []
        y_list = []
        for coor in data[indexes]:
            x = coor[0]
            y = coor[1]
            theta = math.atan2(coor[3], coor[2])
            print(str(x) + '   ' + str(y) + '     ' + str(theta))

            x_list.append(x)
            y_list.append(y)

            rec = Rectangle((x - l/2, y - w/2), l, w ,color='blue', fc = 'None', alpha=0.3 ,lw = 0.8)

            print(math.degrees(theta))

            trafo = mpl.transforms.Affine2D().rotate_around(x,y,theta)
            rec.set_transform(trafo)

            plt.gca().add_patch(rec)

            plot_point((x,y),theta,l/2)
        plt.plot(x_list,y_list,'.')


im = plt.imread('./server_out/strive-scenario-replay-adv-sucess-data/scene_0005_001/scene_0005_001_empty.png')


print(len(im))

# fig, ax = plt.subplots()
# im = ax.imshow(im)
im = plt.imshow(np.flipud(plt.imread('./server_out/strive-scenario-replay-adv-sucess-data/scene_0005_001/scene_0005_001_empty.png')), origin='lower', extent=[0,720,0,720],aspect='1')
# plt.imshow(im, origin='lower')


# x = [20]
# y = [20]
# plt.plot(x, y, marker="o", markersize=5, markerfacecolor="red")




# plt.show()


plt.xlim([0, 720])
plt.ylim([0, 720])


# plt.xticks([])
# plt.yticks([])

# plt.set_axis_off()
plt.tight_layout()
plt.axis('off')

fig = plt.gcf()
DPI = fig.get_dpi()
print(DPI)

# fig.set_size_inches(1014.0/float(DPI),1014.0/float(DPI)) # for 900px
fig.set_size_inches(811.0/float(DPI),811.0/float(DPI)) # for 720px
# plt.show()

plt.savefig('./out/test/scene-0029_empty_720.png', bbox_inches='tight', dpi='figure',pad_inches = 0)



