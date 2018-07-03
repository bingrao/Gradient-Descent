import numpy as np
import pandas as pd
from ggplot import *

area = np.array([30, 35, 37, 59, 70, 76, 88, 100]).astype(np.float32)
price = np.array([1100, 1423, 1377, 1800, 2304, 2588, 3495, 4839]).astype(np.float32)


data_1 = {"area": pd.Series(area), "price": pd.Series(price)}

df_1 = pd.DataFrame(data_1)

p_1 = ggplot(aes(x="area", y="price"), data=df_1) + \
    geom_point() + \
    labs(title="House Price Data", x="Area", y="Price")

max_area = max(area)
min_area = min(area)

max_price = max(price)
min_price = min(price)

# Normalize data
for i in range(0, len(area)):
    area[i] = (area[i] - min_area)/(max_area - min_area)

for j in range(0, len(price)):
    price[j] = (price[j] - min_price)/(max_price - min_area)


data_2 = {"area": pd.Series(area), "price": pd.Series(price)}
df_2 = pd.DataFrame(data_2)

p = ggplot(aes(x="area", y="price"), data=df_2) + \
    geom_point() + \
    labs(title="House Price Data", x="Area", y="Price")




