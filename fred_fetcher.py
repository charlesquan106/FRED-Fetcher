import os
import pandas as pd
from fredapi import Fred
from datetime import datetime
import pyarrow.parquet as pq

# FRED API Key - 需要替換成你自己的API鍵
fred_api_key = '8246cf7657ff4097fab8a70cb1e3de1a'
fred = Fred(api_key=fred_api_key)

# 定義要抓取的數據ID
series_ids = ['UMCSENT', 'ICSA', 'DFF', 'DTB4WK', 'DTB3', 'DTB6', 'DTB1YR', 'DGS6MO',
              'DGS1', 'DGS2', 'DGS3', 'DGS5', 'DGS7', 'DGS10', 'DGS30'
]

# 獲取當前時間並創建資料夾
folder_name = datetime.now().strftime('%Y-%m-%d')
os.makedirs(folder_name, exist_ok=True)

# 對於每個ID，抓取最新資料並存儲為Parquet檔案
for series_id in series_ids:
    data = fred.get_series(series_id)
    df = data.reset_index().rename(columns={'index': 'date', 0: 'value'})
    
    file_path = os.path.join(folder_name, f'{series_id}.parquet')
    df.to_parquet(file_path, engine='pyarrow', index=False)

print(f"資料已經存儲到資料夾: {folder_name}")