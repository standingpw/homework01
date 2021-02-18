def func_predict(x):
    threshes=[]
    for i in range(len(x)):
        threshes.append(x[i]-0.5)
    return threshes