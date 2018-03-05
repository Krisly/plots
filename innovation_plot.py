# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
from matplotlib import image, patches, colors
from matplotlib.colors import colorConverter
import numpy as np

imsize = np.array([319, 217])
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
          (max_radius/1.5, 150, 270, '#ff6100'),
          (max_radius/3, 270, 390, '#000cff'),
          #(96, 45, 58, '#FD7C1A'),
          #(73, 291, 308, '#CCFF28'),
          #(47, 146, 155, '#28FFCC'),
          #(25, 340, 360, '#004AFF')
           ]

for (radius, theta1, theta2, color) in wedges:
    ax.add_patch(patches.Wedge(center, radius, theta1, theta2,
                               fc=color, ec='black', alpha=0.8, zorder=3))

for patch in ax.patches:
    patch.set_clip_path(clip_path)
ax.text(108.5+max_radius * np.cos(np.pi/4),
        108.5+max_radius * np.sin(-np.pi/4), u'Readines')
ax.text(108.5+max_radius * np.cos(np.pi + np.pi/4),
        108.5+max_radius*np.sin(np.pi + np.pi/4), u'Diffuculty')
ax.text(108.5+max_radius * np.cos(6*np.pi/4),
        108.5+max_radius*np.sin(-6*np.pi/4), u'Need')
ax.set_xlim(0, imsize[0])
ax.set_ylim(imsize[1], 0)

plt.show()