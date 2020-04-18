import numpy as np


def most_common(a):
    res = dict((a.count(i), i) for i in set(a))
    return res[max(res.keys())]


arr = np.random.randint(1, 10, (4, 4))
print(arr)
print(most_common(arr))