import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression


x = np.array([10000, 20000, 40000, 80000, 160000])
y = np.array([
    9.84,
    19.36,
    39.18,
    78.95,
    158.67
])

lx = np.log2(x)
ly = np.log2(y)

model = LinearRegression().fit(lx.reshape(-1, 1), ly)
print('slope: ', model.coef_)

lx = sm.add_constant(lx)
res = sm.OLS(ly, lx).fit()
print('intervalo: ', res.conf_int(0.05)[1])
