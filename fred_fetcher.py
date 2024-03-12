import os
from datetime import datetime
from fredapi import Fred
import pandas as pd

# 你的 FRED API 金鑰
api_key = '8246cf7657ff4097fab8a70cb1e3de1a'
fred = Fred(api_key=api_key)

# 指標列表
series_ids = [
    'UMCSENT', 'ICSA', 'DFF', 'DTB4WK', 'DTB3', 'DTB6', 'DTB1YR',
    'DGS6MO', 'DGS1', 'DGS2', 'DGS3', 'DGS5', 'DGS7', 'DGS10',
    'DGS30'
]

# 獲取當前時間並格式化為 ISO 格式的資料夾名稱（僅日期部分）
folder_name = datetime.now().strftime('%Y-%m-%d')
# 在當前目錄下創建以當前時間命名的資料夾
os.makedirs(folder_name, exist_ok=True)

# 抓取數據並存成 Parquet 檔案
for series_id in series_ids:
    try:
        # 抓取數據
        data = fred.get_series(series_id)
        
        # 轉換為 DataFrame
        df = pd.DataFrame(data, columns=['value'])
        df['date'] = df.index
        
        # 存成 Parquet 檔案到指定資料夾
        file_path = os.path.join(folder_name, f'{series_id}.parquet')
        df.to_parquet(file_path)
        print(f'{series_id} 已存成 Parquet 檔案至 {folder_name}。')
    except Exception as e:
        print(f'無法抓取 {series_id} 的數據：{e}')
