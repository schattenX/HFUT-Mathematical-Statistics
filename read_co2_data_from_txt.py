import csv

# 定义输入和输出文件路径
input_file = "data/co2 from 1958-2024.txt"
output_file = "data/co2_data.csv"

# 打开输入文件进行读取
with open(input_file, "r") as file:
    lines = file.readlines()

# 打开输出 CSV 文件进行写入
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # 写入 CSV 文件的表头
    writer.writerow([
        "Year", "Month", "Decimal_Date", "Monthly_Average",
        "De_Seasonalized", "Days", "St_Dev", "Uncertainty"
    ])

    # 处理文件中的每一行
    for line in lines:
        # 跳过注释和空行
        if line.strip() == "" or line.startswith("#"):
            continue

        # 使用空格分割行数据
        columns = line.split()

        # 检查数据长度是否满足要求
        if len(columns) < 8:
            continue

        try:
            # 提取数据字段
            year = int(columns[0])
            month = int(columns[1])
            decimal_date = float(columns[2])
            monthly_average = float(columns[3])
            de_seasonalized = float(columns[4])
            days = int(columns[5])
            st_dev = float(columns[6])
            uncertainty = float(columns[7])

            # 写入 CSV 文件
            writer.writerow([
                year, month, decimal_date, monthly_average,
                de_seasonalized, days, st_dev, uncertainty
            ])
        except ValueError:
            # 忽略无法转换的行
            continue

print(f"数据已成功提取并保存至：{output_file}")
