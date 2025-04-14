import pandas as pd

file_path = "./Data/health_lifestyle.csv"
df = pd.read_csv(file_path)

df.info(), df.head()
