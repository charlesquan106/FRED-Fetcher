from fredapi import Fred
# 設定 API Key
api_key = '8246cf7657ff4097fab8a70cb1e3de1a'
fred = Fred(api_key=api_key)
data = fred.get_series('DGS10')  # 美國十年期公債殖利率

print(fred.get_series_info('DGS10').title)
print(data)

import matplotlib.pyplot as plt
%matplotlib inline

data.plot()
plt.grid()
plt.show()