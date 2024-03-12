import os
import pandas as pd
from fredapi import Fred
from datetime import datetime
import pyarrow.parquet as pq
# 替換為包含Parquet文件的資料夾路徑
folder_path = os.path.join("./2024-03-13/")

# 列出所有Parquet文件
parquet_files = [f for f in os.listdir(folder_path) if f.endswith('.parquet')]

# 依次讀取每個Parquet文件
for file in parquet_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_parquet(file_path)
    print(f"Contents of {file}:")
    print(df)
    print("\n")
