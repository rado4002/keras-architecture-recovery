import inspect
from keras import layers, models, ops


print("Dense layer module:", inspect.getmodule(layers.Dense))
print("Model module:", inspect.getmodule(models.Model))
print("Ops module:", inspect.getmodule(ops))