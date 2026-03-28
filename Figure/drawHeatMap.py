import math

import numpy as np
import pandas as pd

# 读取相似度矩阵数据
import torch
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
import torch.nn.functional as F
from scipy.cluster.hierarchy import linkage, dendrogram

file_path = "result.csv"
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# 解析数据
head_matrix = None
tail_matrix = None
for line in lines:
    parts = line.strip().split("\t")  # 按 Tab 拆分
    if "Head3" in parts[0]:
        sim_matrix1_str = parts[1]  # 获取存储的矩阵字符串
        sim_matrix1 = np.array([float(x) for x in sim_matrix1_str.split(",")])  # 转换回数组
        N = int((len(sim_matrix1))/64)  # 计算 N
        head_matrix = sim_matrix1.reshape((N, 64))

        pd.DataFrame(head_matrix).to_csv("head_result3.csv",index=False,header=False)

    elif "Tail3" in parts[0]:
        sim_matrix2_str = parts[1]
        sim_matrix2 = np.array([float(x) for x in sim_matrix2_str.split(",")])
        N = int((len(sim_matrix2))/64)
        tail_matrix = sim_matrix2.reshape((N, 64))
        pd.DataFrame(tail_matrix).to_csv("tail_result3.csv", index=False, header=False)



