import numpy as np
from sklearn.manifold import TSNE
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Parameters
A_size = 200,10 # 20*10**3,10**2
n_components = 3

# # Randomly generate A
# A = (10**3)*np.random.rand(A_size[0],A_size[1])
# A = A.astype(int)

A = np.zeros(A_size)
for i in range (A_size[0]):
    A[i] = i*np.ones(A_size[1])

# print(A)

# Label

label = list(i for i in range(A_size[0]))

# TSNE

tsne = TSNE(n_components)
tsne_result = tsne.fit_transform(A)
# print(tsne_result.shape)
# print(tsne_result)

tsne_result_data = pd.DataFrame(
    {'tsne_1': tsne_result[:,0],
    'tsne_2': tsne_result[:,1],
    'tsne_3': tsne_result[:,2],
    'label': label
    })

print(tsne_result_data)

# # 2D Display
# fig , ax = plt.subplots()
# sns.scatterplot(
#     x = 'tsne_1',
#     y = 'tsne_2',
#     hue ='label',
#     data = tsne_result_data,
#     ax = ax,
#     s = 120
#     )
# ax.set_aspect('equal')
# plt.show()

# 3D Display - Test 1
fig = plt.figure()
ax = plt.axes(projection ='3d')

x = tsne_result_data['tsne_1']
y = tsne_result_data['tsne_2']
z = tsne_result_data['tsne_3']

ax.set_xlabel("tsne_1")
ax.set_ylabel("tsne_2")
ax.set_zlabel("tsne_3")

ax.scatter(x, y, z,c=label)

ax.legend(label)
plt.show()

# 3D Display - Test 2
fig = plt.figure()
ax = plt.axes(projection ='3d')

sns.scatterplot(
    x = 'tsne_1',
    y = 'tsne_2',
    hue ='label',
    data = tsne_result_data,
    ax = ax
    )

plt.show()