import os

os.environ.setdefault("KERAS_BACKEND", "tensorflow")

import keras
import pkgutil

def main():
    print("Top level Keras modules:\n")
    for module in pkgutil.iter_modules(keras.__path__):
        print(module.name)


if __name__ == "__main__":
    main()