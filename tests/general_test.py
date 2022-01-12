def func(x):
    return x + 1

def test_numpy():
    import numpy as np
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = a + b
    assert np.array_equal(c, np.array([5, 7, 9]))

def test_matplot():
    import matplotlib.pyplot as plt
    x = [1, 2, 3]
    y = [4, 5, 6]
    plt.plot(x, y)

def test_answer():
    assert func(4) == 5