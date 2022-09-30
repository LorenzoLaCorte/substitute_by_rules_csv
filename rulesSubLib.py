import pandas as pd

class TableModifier:
    def __init__(self, table_file: str, number_rule_path:str, regions_rule_path:str,
                modified_path:str, frequency_path:str) -> None:
        self.table_file = table_file
        self.number_rule_path= number_rule_path
        self.regions_rule_path = regions_rule_path
        self.modified_path = modified_path
        self.frequency_path = frequency_path

    def modifyByRules(self) -> None:
        tableData = pd.read_csv(self.table_file)
        dictRegions= pd.read_csv(self.number_rule_path, header=None, dtype={0: str}).set_index(0).squeeze().to_dict()
        rulesNumbers = pd.read_csv(self.regions_rule_path)

        listNumbers = []
        for singleRange in rulesNumbers.iloc[0]:
            listNumbers.append(singleRange)

        for i in range(tableData.shape[0]):
            for j in range(tableData.shape[1]):
                key = tableData.iloc[i, j]
                if key in dictRegions:
                    tableData.iloc[i, j] = dictRegions[key]
                else:
                    key = int(key)
                    for rang in listNumbers:
                        if(key >= int(rang.split('-')[0]) and key <= int(rang.split('-')[1])):
                            tableData.iloc[i, j] = rang
                            
        tableData.to_csv(self.modified_path)

    def computeFrequency(self) -> None:
        tableData = pd.read_csv(self.modified_path)
        tableData_frequency = (tableData.groupby(list(tableData.columns)).size().reset_index(name='Count'))
        tableData_frequency.to_csv(self.frequency_path)