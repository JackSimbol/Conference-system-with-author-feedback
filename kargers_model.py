import numpy as np
import random

def kg_binary(A: np.array, kmax: int):
    X = np.zeros(A.shape, dtype=float)
    Y = np.zeros(A.shape, dtype=float)
    final_x = np.zeros(A.shape[0], dtype=float)
    for i in range(A.shape[0]): 
        for j in range(A.shape[1]):
            if A[i, j] != 0:
                Y[i, j] = random.sample([1,-1], 1)[0]
    for k in range(kmax):
        for i in range(A.shape[0]):
            sum_row_y = np.sum(A[i]*Y[i])
            for j in range(A.shape[1]):
                if A[i][j] != 0:
                    X[i][j] = sum_row_y - A[i][j] * Y[i][j]
        for j in range(A.shape[1]):
            sum_col_x = np.sum(A[:,j]*X[:,j])
            for i in range(A.shape[0]):
                if A[i][j] != 0:
                    Y[i][j] = sum_col_x - A[i][j] * X[i][j]
    for i in range(A.shape[0]):
        final_x[i] = np.sum(A[i]*Y[i])
    
    return np.sign(final_x)

def kg_binary_with_init(A: np.array, kmax: int, init: np.array):
    X = np.zeros(A.shape, dtype=float)
    Y = np.zeros(A.shape, dtype=float)
    final_x = np.zeros(A.shape[0], dtype=float)
    for i in range(A.shape[0]): 
        for j in range(A.shape[1]):
            if A[i, j] != 0:
                Y[i, j] = init[j]
    for k in range(kmax):
        for i in range(A.shape[0]):
            sum_row_y = np.sum(A[i]*Y[i])
            for j in range(A.shape[1]):
                if A[i][j] != 0:
                    X[i][j] = sum_row_y - A[i][j] * Y[i][j]
        for j in range(A.shape[1]):
            sum_col_x = np.sum(A[:,j]*X[:,j])
            for i in range(A.shape[0]):
                if A[i][j] != 0:
                    Y[i][j] = sum_col_x - A[i][j] * X[i][j]
    for i in range(A.shape[0]):
        final_x[i] = np.sum(A[i]*Y[i])
    
    return final_x        

def kg_binary_with_assist(A: np.array, kmax: int, assist: np.array):
    X = np.zeros(A.shape, dtype=float)
    Y = np.zeros(A.shape, dtype=float)
    final_x = np.zeros(A.shape[0], dtype=float)
    for i in range(A.shape[0]): 
        for j in range(A.shape[1]):
            if A[i, j] != 0:
                Y[i, j] = random.sample([1,-1], 1)[0]
    for k in range(kmax - 1):
        for i in range(A.shape[0]):
            sum_row_y = np.sum(A[i]*Y[i])
            for j in range(A.shape[1]):
                if A[i][j] != 0:
                    X[i][j] = sum_row_y - A[i][j] * Y[i][j]
        for j in range(A.shape[1]):
            sum_col_x = np.sum(A[:,j]*X[:,j])
            for i in range(A.shape[0]):
                if A[i][j] != 0:
                    Y[i][j] = sum_col_x - A[i][j] * X[i][j]
    # merge the iterative results with the assist info
    for j in range(A.shape[1]):
        Y[:j] += assist
        #Y[:j] *= assist
    for i in range(A.shape[0]):
        final_x[i] = np.sum(A[i]*Y[i])
    
    return final_x        

def kg_binary_with_lambda_assist(A: np.array, kmax: int, assist: np.array, lamBda: float):
    X = np.zeros(A.shape, dtype=float)
    Y = np.zeros(A.shape, dtype=float)
    final_x = np.zeros(A.shape[0], dtype=float)
    for i in range(A.shape[0]): 
        for j in range(A.shape[1]):
            if A[i, j] != 0:
                Y[i, j] = random.sample([1,-1], 1)[0]
    for k in range(kmax - 1):
        for i in range(A.shape[0]):
            sum_row_y = np.sum(A[i]*Y[i])
            for j in range(A.shape[1]):
                if A[i][j] != 0:
                    X[i][j] = sum_row_y - A[i][j] * Y[i][j]
        for j in range(A.shape[1]):
            sum_col_x = np.sum(A[:,j]*X[:,j])
            for i in range(A.shape[0]):
                if A[i][j] != 0:
                    Y[i][j] = sum_col_x - A[i][j] * X[i][j]
    # merge the iterative results with the assist info
    for j in range(A.shape[1]):
        Y[:j] += lamBda*assist
        #Y[:j] *= assist
    for i in range(A.shape[0]):
        final_x[i] = np.sum(A[i]*Y[i])
    
    return final_x 