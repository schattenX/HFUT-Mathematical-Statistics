import csv

# 定义输入和输出文件路径
input_file = "data/land-ocean index from 1880-2023.txt"
output_file = "data/land_ocean_temperature_index.csv"

# 打开输入文件进行读取
with open(input_file, "r") as file:
    lines = file.readlines()

# 打开输出 CSV 文件进行写入
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # 写入 CSV 文件的表头
    writer.writerow(["Year", "No_Smoothing", "Lowess_5"])

    # 处理文件中的每一行
    for line in lines:
        # 跳过注释和空行
        if line.strip() == "" or line.startswith("-") or line.startswith("Year"):
            continue

        # 使用空格分割行数据
        columns = line.split()

        # 检查数据长度是否满足要求
        if len(columns) != 3:
            continue

        try:
            # 提取数据字段
            year = int(columns[0])
            no_smoothing = float(columns[1])
            lowess_5 = float(columns[2])

            # 写入 CSV 文件
            writer.writerow([year, no_smoothing, lowess_5])
        except ValueError:
            # 忽略无法转换的行
            continue

print(f"数据已成功提取并保存至：{output_file}")
