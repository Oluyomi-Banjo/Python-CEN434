import pandas as pd

data = {'x': [1,2,3,4,5], 'y': [2,4,6,8,10]}
df = pd.DataFrame(data)
print(df)
a = df.to_numpy()
print(a)

a.reshape(2,5)
a.reshape(5,2)
