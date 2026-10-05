# Cmput 455 sample code
# 2-layer neural network
# Adapted from http://iamtrask.github.io/2015/07/12/basic-python-network
# Converted to Python3 and adapted for Cmput 455 by Martin Mueller

from typing import List, Tuple
import numpy as np

Float = np.float64
FloatArray = np.typing.NDArray[Float]

def sigmoid(x: FloatArray) -> FloatArray:
    """Activation function: maps inputs to (0, 1)."""
    return 1.0 / (1.0 + np.exp(-x))

def sigmoid_derivative(sigma: FloatArray) -> FloatArray:
    """Derivative of sigmoid in terms of the output sigma = sigmoid(x)."""
    return sigma * (1.0 - sigma)

def train_single_layer(
    X: FloatArray,
    y: FloatArray,
    num_iterations: int = (1 << 20) + 1,
    seed: int = 1
) -> None:
    """Train a single hidden layer neural network using gradient descent."""
    rng = np.random.default_rng(seed)
    
    # Hidden layer weights (3 inputs -> 1 output) initialized in range [-1, 1]
    syn0: FloatArray = 2.0 * rng.random((X.shape[1], 1)) - 1.0

    next_print_time = 1
    l1: FloatArray = np.zeros_like(y)

    for i in range(num_iterations):
        # Forward propagation
        l0 = X
        l1 = sigmoid(np.dot(l0, syn0))

        # Error evaluation
        l1_error = y - l1

        # Gradient calculation
        l1_delta = l1_error * sigmoid_derivative(l1)

        # Update weights
        syn0 += np.dot(l0.T, l1_delta)

        if i >= next_print_time:
            mse = np.mean((y - l1) ** 2)
            print(f"Iteration {i}\nl1:\n{l1}\nl1_error:\n{l1_error}")
            print(f"Mean square error: {mse}\n")
            next_print_time *= 2

def test_input() -> FloatArray:
    # Input (4 samples, 3 features)
    return np.array([
        [0, 0, 1],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ], dtype=Float)

def test_output(test_case: int) -> FloatArray:
    # Desired output
    data: List[float]
    if test_case == 1:
        # easy example, just learn that Y = X[0]
        data = [0, 0, 1, 1]
    elif test_case == 2:
        # hard example. This simple net does not learn it perfectly
        data = [0, 1, 1, 0]
    else:
        # hard example. This simple net does not learn it perfectly
        data = [0,1,0.3,0.5]
    return np.array([data], dtype=Float).T

if __name__ == "__main__":
    test_case = 3
    X = test_input()    
    y = test_output(test_case)
    train_single_layer(X, y)