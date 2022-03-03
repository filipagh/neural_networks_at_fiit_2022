

print("tensor")
import tensorflow as tf
print(tf.__version__)

print("")
print("")

print("torch")

import torch
print(torch.version.__version__)
print(torch.version.cuda)
print(torch.cuda.is_available())
t = torch.ones(10)
t.to("cpu")
print(t)
