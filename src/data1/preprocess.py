import pandas as pd

# Assuming you have a Parquet file named 'example.parquet'
file_path = 'D:\\Masters_Courses\\ELG5255_Applied_Machine_Learning\\Project_NAPS\\NAPS\\data\\train_series.parquet'

# Reading the Parquet file into a pandas DataFrame
df = pd.read_parquet(file_path)

# Displaying the contents of the DataFrame
print(df)
