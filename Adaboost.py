import numpy as np
#import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import math
from func_predict import *
x = [0,1,2,3,4,5,6,7,8,9]
y = [1,1,1,-1,-1,-1,1,1,1,-1]
w_1 = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
print('x的长度'+str(len(x)))
print('y的长度'+str(len(y)))
print('w的长度'+str(len(w_1)))
threshes = func_predict(x)
threshes1 = func_predict(x)
print(threshes)