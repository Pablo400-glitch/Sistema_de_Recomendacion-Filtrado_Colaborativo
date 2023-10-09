import numpy as np

items = np.array([[5, 3, 4, 4, "-"],
                  [3, 1, 2, 3, 3],
                  [4, 3, 4, 3, 5],
                  [3, 3, 1, 5, 4],
                  [1, 5, 5, 2, 1]])

item1 = items[1:, 0].astype(int)
item2 = items[1:, 1].astype(int)
item3 = items[1:, 2].astype(int)
item4 = items[1:, 3].astype(int)
item5 = items[1:, 4].astype(int)

print("Correlacion entre item5 y item1")
item5_item1_corr = np.corrcoef(item5, item1)
print(item5_item1_corr[0,1])

print("Correlacion entre item5 y item2")
item5_item2_corr = np.corrcoef(item5, item2)
print(item5_item2_corr[0,1])

print("Correlacion entre item5 y item3")
item5_item3_corr = np.corrcoef(item5, item3)
print(item5_item3_corr[0,1])

print("Correlacion entre item5 y item4")
item5_item4_corr = np.corrcoef(item5, item4)
print(item5_item4_corr[0,1])

mean_item1 = np.mean(item1)
mean_item4 = np.mean(item4)
mean_item5 = np.mean(item5)

num = (item5_item1_corr[0,1] * (items[0, 0].astype(int) - mean_item1)) + (item5_item4_corr[0,1] * (items[0, 2].astype(int) - mean_item4))
den = item5_item1_corr[0,1] + item5_item4_corr[0,1]
r = mean_item5 + num / den

print(r)