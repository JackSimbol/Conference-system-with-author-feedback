import numpy as np
from kargers_model import kg_binary, kg_binary_with_init, kg_binary_with_assist, kg_binary_with_lambda_assist

def majority_vote(A: np.array):
    X = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        X[i] = np.sum(A[i])
    return X

def Karger_I(A: np.array, k_max: int):
    return kg_binary(A, k_max)

def Karger_II(A_1: np.array, A_2: np.array, k_1: int, k_2: int):
    # A_1: paper_review
    # A_2: review_report
    reviewer_init = kg_binary(A_2, k_2)
    return kg_binary_with_init(A_1, k_1, reviewer_init)

def Karger_III(A_1: np.array, A_2: np.array, k_1: int, k_2: int):
    # A_1: paper_review
    # A_2: review_report
    reviewer_init = kg_binary(A_2, k_2)
    return kg_binary_with_assist(A_1, k_1, reviewer_init)

def majority_vote_II(A_1: np.array, A_2: np.array):
    Y = np.zeros(A_2.shape[0])
    for i in range(A_2.shape[0]):
        Y[i] = np.sum(A_2[i])
    Y = (Y-np.min(Y))/(np.max(Y)-np.min(Y))*2-1
    Y = np.sign(Y)
    X = np.zeros(A_1.shape[0])
    for i in range(A_1.shape[0]):
        X[i] = np.sum(A_1[i]*Y)
    return X

def Karger_IV(A_1: np.array, A_2: np.array, k_1: int, k_2: int, paper_per_reviewer):
    assist = kg_binary(A_2, k_2)
    consistency = 0
    for i in range(assist.shape[0]):
        consistency += sum(A_2[i])*assist[i]
    consistency /= (paper_per_reviewer*assist.shape[0])
    return kg_binary_with_lambda_assist(A_1, k_1, assist, consistency)