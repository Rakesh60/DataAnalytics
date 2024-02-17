import pandas as pd
dis={"A":[1,2,3,4,5,6,],"B":[1,2,3,4,5,6],"C":[1,2,3,4,5,6]}

data=pd.DataFrame(dis)
print(data)
data.to_csv('my_file.csv')