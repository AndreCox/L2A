import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

keras.datasets.mnist.load_data(path="mnist.npz")


def train():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    assert x_train.shape == (60000, 28, 28)
    assert x_test.shape == (10000, 28, 28)
    assert y_train.shape == (60000,)
    assert y_test.shape == (10000,)

    # Normalize the data
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    # Convert the labels to one-hot encoding
    y_train = keras.utils.to_categorical(y_train, 10)
    y_test = keras.utils.to_categorical(y_test, 10)

    # Define the model
    model = keras.models.Sequential(
        [
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation="relu"),
            keras.layers.Dense(10, activation="softmax"),
        ]
    )

    # Compile the model
    model.compile(
        optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
    )

    # Train the model
    model.fit(x_train, y_train, batch_size=128, epochs=10, validation_split=0.2)

    # Evaluate the model
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print("Test accuracy:", test_acc)

    # Save the model
    model.save("mnist.h5")


def test():
    # Load the model
    model = keras.models.load_model("mnist.h5")

    # Display a random image from the test set
    idx = np.random.randint(0, 10000)
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0
    image = x_test[idx]
    plt.imshow(image, cmap="gray")

    # Predict the image
    prediction = model.predict(np.array([image]))
    print("Prediction:", np.argmax(prediction[0]))
    plt.show()


# main loop
if __name__ == "__main__":
    # command line arguments
    import sys

    # if argument is -c, test the model else train the model
    if sys.argv[1] == "-c":
        print("Testing the model...")
        test()
    elif sys.argv[1] == "-t":
        print("Training the model...")
        train()
