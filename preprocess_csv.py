import pandas as pd
import csv

def preprocess_csv(input_file, output_file):
    """预处理CSV文件，去除空白列"""
    # 读取原始CSV文件
    with open(input_file, 'r', encoding='gbk') as f:
        lines = f.readlines()
    
    # 处理每一行，将,,替换为,
    processed_lines = []
    for line in lines:
        # 将多个连续逗号替换为单个逗号
        import re
        processed_line = re.sub(r',,+', ',', line)
        processed_lines.append(processed_line)
    
    # 写入处理后的文件
    with open(output_file, 'w', encoding='gbk') as f:
        f.writelines(processed_lines)
    
    print(f"预处理完成！")
    print(f"原始文件: {input_file}")
    print(f"处理后文件: {output_file}")
    
    # 显示处理前后的对比
    print("\n处理前（第一行）:")
    print(lines[0].strip())
    print("\n处理后（第一行）:")
    print(processed_lines[0].strip())
    
    return output_file

# 使用示例
if __name__ == "__main__":
    input_csv = "./test.csv"
    output_csv = "./test_processed.csv"
    
    processed_file = preprocess_csv(input_csv, output_csv)
    
    # 验证处理结果
    print("\n验证处理结果:")
    with open(processed_file, 'r', encoding='gbk') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(f"列名: {header}")
        print(f"列数: {len(header)}")
        
        # 显示前几行数据
        print("\n前3行数据:")
        for i, row in enumerate(reader):
            if i < 3:
                print(row)
            else:
                break