# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
from matplotlib import image, patches, colors
from matplotlib.colors import colorConverter
import numpy as np

# Sets Plotting parameters
font_size = 15
plt.rcParams['figure.figsize'] = (10,20)
plt.rc('font',   size=font_size)       # controls default text sizes
plt.rc('axes',  titlesize=font_size)   # fontsize of the axes title
plt.rc('axes',   labelsize=font_size)  # fontsize of the x any y labels
plt.rc('xtick',  labelsize=font_size)  # fontsize of the tick labels
plt.rc('ytick',  labelsize=font_size)  # fontsize of the tick labels
plt.rc('legend', fontsize=font_size)   # legend fontsize
plt.rc('figure', titlesize=font_size)  # # size of the figure title

imsize = np.array([319, 237])
center = [108.5, 108.5]
max_radius = 108
radii = np.linspace(16, max_radius, 5)
angles = np.arange(0, 360, 45)


fig = plt.figure(figsize=imsize / 50.)
ax = fig.add_axes([0, 0, 1, 1], frameon=False, xticks=[], yticks=[])


# Create a clip path for the elements
clip_path = patches.Rectangle((0, 0), imsize[0], imsize[1],
                              transform=ax.transData)

# Create the background gradient
x = np.array([0, 104, 196, 300])
y = np.linspace(150, 450, 86)[:, None]

c = np.cos(-np.pi / 4)
s = np.sin(-np.pi / 4)
X, Y = (c * x - s * y) - 116, (s * x + c * y)
C = np.arange(255).reshape((3, 85)).T
C = C[::-1, :]
'''

'''
# plot circles and lines
for radius in radii:
    ax.add_patch(patches.Circle(center, radius, lw=0.5,
                                ec='gray', fc='none', zorder=2))
for angle in angles:
    dx, dy = np.sin(np.radians(angle)), np.cos(np.radians(angle))
    ax.plot([max_radius * (1 - dx), max_radius * (1 + dx)],
            [max_radius * (1 - dy), max_radius * (1 + dy)],
            '-', color='gray', lw=0.5, zorder=2)

# plot wedges within the graph
wedges = [
          (max_radius/2, 30,150, '#00ff08'),
          (max_radius/3, 150, 270, '#ff6100'),
          (max_radius/1.8, 270, 390, '#000cff'),
          (max_radius/1.6, 30,150, '#00ff08'),
          (max_radius/2.5, 150, 270, '#ff6100'),
          (max_radius/1.4, 270, 390, '#000cff'),
          #(25, 340, 360, '#004AFF')
           ]
def transp(i):
    if i < 3:
        return 0.8
    else:
        return 0.6
i=0
for (radius, theta1, theta2, color) in wedges:
    ax.add_patch(patches.Wedge(center,
                               radius,
                               theta1,
                               theta2,
                               fc=color,
                               ec='black',
                               alpha=transp(i),
                               zorder=3))
    i+=1

for patch in ax.patches:
    patch.set_clip_path(clip_path)

ax.text(110+max_radius * np.cos(np.pi/4),
        108.5+max_radius * np.sin(-np.pi/4), u'TRL')
ax.text(80+max_radius * np.cos(np.pi + np.pi/4),
        108.5+max_radius*np.sin(np.pi + np.pi/4), u'R&D3')
ax.text(108.5+max_radius * np.cos(6*np.pi/4),
        120+max_radius*np.sin(-6*np.pi/4), u'TNV')

ax.text(108.5 + 0.76*max_radius * np.cos(np.pi/4),
        108.5 + 0.76*max_radius * np.sin(-np.pi/4), u'5')
ax.text(108.5 + 0.5*max_radius * np.cos(np.pi + np.pi/4),
        108.5 + 0.5*max_radius * np.sin(np.pi + np.pi/4), u'4')
ax.text(108.5 + 0.75*max_radius * np.cos(6*np.pi/4),
        108.5 + 0.75*max_radius * np.sin(-6*np.pi/4), u'3')

ax.text(108.5 + 0.12*max_radius * np.cos(np.pi/4),
        108.5 + 0.12*max_radius * np.sin(-np.pi/4), u'1')
ax.text(108.5 + 0.12*max_radius * np.cos(np.pi + np.pi/4),
        108.5 + 0.12*max_radius * np.sin(np.pi + np.pi/4), u'5')
ax.text(108.5 + 0.12*max_radius * np.cos(6*np.pi/4),
        108.5 + 0.12*max_radius * np.sin(-6*np.pi/4), u'5')

ax.text(108.5 + 0.92*max_radius * np.cos(np.pi/4),
        108.5 + 0.92*max_radius * np.sin(-np.pi/4), u'9')
ax.text(108.5 + 0.95*max_radius * np.cos(np.pi + np.pi/4),
        108.5 + 0.95*max_radius * np.sin(np.pi + np.pi/4), u'1')
ax.text(108.5 + 0.95*max_radius * np.cos(6*np.pi/4),
        108.5 + 0.95*max_radius * np.sin(-6*np.pi/4), u'1')

ax.text(250, 108.5, u'Critical',color='r')
#ax.text(108.5-45, -10, u'Risk Diagram',size=20)
ax.set_xlim(0, imsize[0])
ax.set_ylim(imsize[1], 0)

plt.savefig('/home/kristoffer/Desktop/Github/plots/innovation_plot.pdf')
plt.show()