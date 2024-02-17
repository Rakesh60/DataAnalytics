import pandas as pd

csv1=pd.read_csv('spdata.csv',dtype={"MRP":"float"})

print(csv1)

