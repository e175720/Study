import sys, os

sys.path.append(os.pardir)

import numpy as np

from MNIST_data import 

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_test.shape)
print(t_train.shape)