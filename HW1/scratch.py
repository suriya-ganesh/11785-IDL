import math
import random
import numpy as np
import numpy.random

```
simulation for quiz
```

running_average_sum = 0
totaldiv = []
for researcher in range(50):

    sum = 0
    divergences = []
    print("!!",numpy.random.exponential(10))
    for datapoint in range(1000):
        divergences.append(numpy.random.exponential(10)/2)
    totaldiv.extend(divergences)
    variance = np.var(divergences, axis=0)
    print(variance)
print(np.var(totaldiv, axis=0))
# print(running_average_sum/ 5)
# print()
