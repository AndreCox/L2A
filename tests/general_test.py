def func(x):
    return x + 1


# Check if python can run basic functions
def test_answer():
    assert func(4) == 5


# Check if numpy is functional
def test_numpy():
    import numpy as np

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = a + b
    assert np.array_equal(c, np.array([5, 7, 9]))


# check if matplotlib is functional
def test_matplot():
    import matplotlib.pyplot as plt

    x = [1, 2, 3]
    y = [4, 5, 6]
    plt.plot(x, y)


# check if pandas is functional
def test_pandas():
    import pandas as pd

    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    assert df["A"].sum() == 6


# check if tensorflow is functional
def test_tensorflow():
    import tensorflow as tf

    if tf.config.list_physical_devices("GPU"):
        print("TensorFlow **IS** using the GPU")
    else:
        print("TensorFlow **IS NOT** using the GPU")
    a = tf.constant([1.0, 2.0, 3.0], shape=[3], name="a")
    b = tf.constant([1.0, 2.0, 3.0], shape=[3], name="b")
    c = a + b
    # check if the sum of a and b equals c using tensorflow v2
    assert tf.reduce_sum(c).numpy() == 12.0


# check if keras is functional
def test_keras():
    import tensorflow.keras as keras
    import numpy as np

    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer="sgd", loss="mean_squared_error")
    xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
    ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)
    model.fit(xs, ys, epochs=500)
    assert model.predict([10.0])[0] > 5.0
