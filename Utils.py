"""
    Some utils functions, mostly vector related.
"""

import numpy as np

# Normalize to 1 a vector
def normalize(v):
    norm = np.linalg.norm(v, ord=1)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm

# Rotate a vector by x degrees
def rotate(v, angle):
    a = np.arctan2(v[0], v[1])
    l = length(v)
    n = (np.radians(angle) + a) % (np.pi * 2)
    return np.multiply(normalize(np.array([np.sin(n), np.cos(n)])), l)

# Get vector angle in degrees
def heading(v):
    return np.degrees(np.arctan2(v[0], v[1]))

# Get the vector length
def length(v):
    return np.linalg.norm(v, ord=1)

# Get the intersection between two lines
def get_intersect(a1, a2, b1, b2):
    s = np.vstack([a1,a2,b1,b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return (x/z, y/z)

# Get the distance between two point vectors
def distance(a, b):
    return np.linalg.norm(a-b)

# Determine if the bounding boxes of two vectors intersects
def points_collide(p1, p2, p3, p4):
    width1 = np.abs(p1[0] - p2[0])
    height1 = np.abs(p1[1] - p2[1])
    if (p1[0] > p2[0]):
        x1 = p2[0]
    else:
        x1 = p1[0]
    if (p1[1] > p2[1]):
        y1 = p2[1]
    else:
        y1 = p1[1]

    width2 = np.abs(p3[0] - p4[0])
    height2 = np.abs(p3[1] - p4[1])
    if (p3[0] > p4[0]):
        x2 = p4[0]
    else:
        x2 = p3[0]
    if (p3[1] > p4[1]):
        y2 = p4[1]
    else:
        y2 = p3[1]

    if (x1 + width1 >= x2 and x1 <= x2 + width2):
        if (y1 + height1 >= y2 and y1 <= y2 + height2):
            return True
    return False

# Determine if p3 is in the bounding box of the vector p2 w/ origin p1
def point_in_line(p1, p2, p3):
    width = np.abs(p1[0] - p2[0])
    height = np.abs(p1[1] - p2[1])
    if (p1[0] > p2[0]):
        x = p2[0]
    else:
        x = p1[0]
    if (p1[1] > p2[1]):
        y = p2[1]
    else:
        y = p1[1]

    if (p3[0] >= x - 2 and p3[0] <= x + width + 2):
        if (p3[1] >= y - 2 and p3[1] <= y + height + 2):
            return True
    return False
