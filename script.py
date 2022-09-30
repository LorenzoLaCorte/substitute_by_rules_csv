import pandas as pd

tableData = pd.read_csv("table.csv")

dictRegions = pd.read_csv('rules/regions.csv', header=None, dtype={0: str}).set_index(0).squeeze().to_dict()

rulesNumbers = pd.read_csv("rules/numbers.csv")

listNumbers = []
for ran in rulesNumbers.iloc[0]:
    listNumbers.append(ran)

for i in range(tableData.shape[0]):
    for j in range(tableData.shape[1]):
        key = tableData.iloc[i, j]
        if key in dictRegions:
            tableData.iloc[i, j] = dictRegions[key]
        else:
            key = int(key)
            for rang in listNumbers:
                if(key >= int(rang.split('-')[0]) and key <= int(ran.split('-')[1])):
                    tableData.iloc[i, j] = rang

tableData.to_csv("output.csv")

tableData_frequency = (tableData.groupby(list(tableData.columns)).size().reset_index(name='Count'))
tableData_frequency.to_csv("output_frequency.csv")