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
