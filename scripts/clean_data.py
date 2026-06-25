import pandas as pd
pd.read_csv("datasets.csv")
data.duplicated().sum()
data.dropna(inplace = True)
data.info()
data.reset_index(inplace = True)
data.drop(columns = "index")
data.to_csv("cleaned_csv.csv")
