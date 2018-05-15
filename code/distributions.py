import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    data = np.random.normal(2360, 950, 12)

    print(data)
    plt.hist(data)
    plt.savefig('test.png')
