import pandas as pd

data = pd.read_csv("datasets.csv")
print("Duplicates found:", data.duplicated().sum())
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)
data.reset_index(inplace=True)
data.drop(columns="index", inplace=True)
data.to_csv("cleaned_csv_fixed.csv", index=False)
print("Final shape:", data.shape)
