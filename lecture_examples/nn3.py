# Cmput 455 sample code
# 3 layer neural network
# Code from http://iamtrask.github.io/2015/07/12/basic-python-network
# Converted to Python3 and adapted for Cmput 455 by Martin Mueller

import numpy as np
from nn import FloatArray, sigmoid, sigmoid_derivative, test_input, test_output
    
def train(
    X: FloatArray,
    y: FloatArray,
    num_iterations: int = (1 << 20) + 1,
    seed: int = 1
) -> None:
    rng = np.random.default_rng(seed)

    # Two hidden layers initialized in range [-1, 1]
    syn0: FloatArray = 2.0 * rng.random((3, 4)) - 1.0
    syn1: FloatArray = 2.0 * rng.random((4, 1)) - 1.0

    next_print_time = 1
    for i in range(num_iterations):

        # Feed forward through layers 0, 1, and 2
        l0 = X
        l1 = sigmoid(np.dot(l0, syn0))
        l2 = sigmoid(np.dot(l1, syn1))

        l2_error = y - l2
    
        if i >= next_print_time:
            next_print_time *= 2
            mean_error: float = float(np.mean(np.abs(l2_error)))
            print(f"Iteration {i} Error: {mean_error}")
        
        l2_delta = l2_error * sigmoid_derivative(l2)
        l1_error = l2_delta.dot(syn1.T)
        l1_delta = l1_error * sigmoid_derivative(l1)

        syn1 += l1.T.dot(l2_delta)
        syn0 += l0.T.dot(l1_delta)

if __name__ == "__main__":
    test_case = 3
    X = test_input()    
    y = test_output(test_case)
    train(X, y)