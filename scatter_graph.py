import pandas as pd
import matplotlib.pyplot as plt
import os

# 读取数据
data = pd.read_csv('data/temperature_co2_data_1970to2023.csv')

# 创建绘图窗口
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制CO₂浓度的散点图（左Y轴）
ax1.set_xlabel('Year')
ax1.set_ylabel('CO₂ Concentration (ppm)', color='blue')
ax1.scatter(data['Year'], data['Monthly_Average'], color='blue', label='CO₂ Concentration (ppm)')
ax1.tick_params(axis='y', labelcolor='blue')

# 创建右侧Y轴并绘制气温异常的散点图
ax2 = ax1.twinx()
ax2.set_ylabel('Temperature Anomaly (°C)', color='red')
ax2.scatter(data['Year'], data['No_Smoothing'], color='red', label='Temperature Anomaly (°C)')
ax2.tick_params(axis='y', labelcolor='red')

# 添加图例和标题
fig.suptitle('Year vs CO₂ Concentration and Temperature Anomaly (1970-2023)')
fig.tight_layout()

save_dir = 'plots/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
plt.savefig(save_dir + 'CO2 and temperature Anomaly.png')

plt.show()
