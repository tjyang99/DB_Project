import pandas as pd
import numpy as np
import math

def calculate_nearest_centroid(r, c):
    alg_data = np.genfromtxt("cluster_centers_1.csv", delimiter=",")
    alg_data_no_head = np.delete(alg_data, 0, 0)
    clean_alg_data = np.delete(alg_data_no_head, 0, 1)
    rows, cols = clean_alg_data.shape
    res = euclidean_distance(r, c, clean_alg_data[0, :])
    recommend = clean_alg_data[0, 0]
    for r in range(1, rows):
        new_res = euclidean_distance(r, c, clean_alg_data[r, :])
        if new_res < res:
            res = new_res
            recommend = clean_alg_data[r, 0]
    return recommend
    
def euclidean_distance(r, c, row):
    return math.pow((float(row[0]) - float(c)), 2) + math.pow((float(row[1]) - float(r)), 2)