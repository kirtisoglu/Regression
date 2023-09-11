import pandas as pd
import numpy as np
from sklearn import linear_model


reg = linear_model.LinearRegression()
data = pd.read_excel('oxygenpurity.xls')

print(data)