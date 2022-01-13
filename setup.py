# install dependencies from requirements.txt
import os

# geT the current working directory
cwd = os.getcwd()
print(cwd)

print("Installing dependencies...")
os.system("pip3 install -r requirements.txt")
print("Dependencies installed.")
print("Installing dev dependencies...")
os.system("pip3 install -r requirements-dev.txt")
print("Dev dependencies installed.")

print("Configuring Hooks...")
os.system("pre-commit install")
print("Hooks configured.")

print("Setup complete.")

print("Testing Installation...")
os.system("pytest -v")
print("Installation tested.")
print("If there are no errors, everthing installed correctly.")

# ask user to press y or n to continue/exit
input = input("Would you like to test gpu suport? (y/n): ")
if input == "y" or input == "Y":
    print("Testing GPU support...")
    import tensorflow as tf

    if tf.config.list_physical_devices("GPU"):
        print("TensorFlow **IS** using the GPU")
    else:
        print("TensorFlow **IS NOT** using the GPU")
else:
    print("Exiting...")
