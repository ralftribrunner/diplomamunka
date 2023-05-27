import pandas as pd
 
dataframe = pd.read_csv("./data-mining-trend/avgFeatures.csv")
 
matrix = dataframe.corr()

print("Correlation Matrix is : ")
print(matrix)

print(matrix.columns)

counter = 0

for i in range(len(matrix.columns)):
    for j in range(i):
        if abs(matrix.iloc[i, j]) > 0.8:
            col1 = matrix.columns[i]
            col2 = matrix.columns[j]
            print(f"{col1} és {col2} között magas korreláció van: {matrix.iloc[i, j]}")
            counter = counter + 1

print(counter)
