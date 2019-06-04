import numpy as np

def normalize(v):
    norm = np.linalg.norm(v, ord=1)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm

def rotate(v, angle):
    a = np.arctan2(v[0], v[1])
    l = length(v)
    n = (np.radians(angle) + a) % (np.pi * 2)
    return np.multiply(normalize(np.array([np.sin(n), np.cos(n)])), l)

def heading(v):
    return np.degrees(np.arctan2(v[0], v[1]))

def length(v):
    return np.linalg.norm(v, ord=1)
