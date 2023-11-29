import pyzipper
import os
import csv
import chardet

def detect_file_encoding(file_path):
    """
    检测文件的编码格式

    参数:
    - file_path: 文件的路径

    返回值:
    - 文件的编码格式
    """
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())

    return result['encoding']


def extract_password_protected_zip(zip_file_path, extract_to_path, password = None):
    """
    解压带密码的 ZIP 文件

    参数:
    - zip_file_path: ZIP 文件的路径
    - extract_to_path: 解压目标路径
    - password: ZIP 文件密码
    """
    with pyzipper.AESZipFile(zip_file_path, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        fname =  zipf.namelist()[0]
        zipf.setpassword(bytes(password,"utf-8"))
        zipf.extractall(extract_to_path)
    return os.path.join(extract_to_path, fname)

def _read_csv_with_header(file_path, header_keyword):
    """
    读取CSV文件内容，以指定的关键词为标志，找到第一个包含交易时间字段的行

    参数:
    - file_path: CSV文件的路径
    - header_keyword: 第一行包含交易时间字段的关键词

    返回值:
    - 一个包含每行数据的列表
    """
    with open(file_path, 'r', newline='', encoding=detect_file_encoding(file_path)) as csv_file:
        csv_reader = csv.reader(csv_file)

        # 找到第一个包含指定关键词的行
        header_index = 0
        for index, row in enumerate(csv_reader):
            if header_keyword in row:
                header_index = index
                break

        # 设置文件指针到找到的行
        csv_file.seek(0)
        for _ in range(header_index):
            next(csv_reader)

        # 读取剩余的数据
        data = [row for row in csv_reader]

    return data

def alipaybill(file_path):
    data = _read_csv_with_header(file_path,'交易时间')
    return data[1:]

def wechatbill(file_path):
    data = _read_csv_with_header(file_path,'交易时间')
    return data[1:]

# 示例用法
csv_file_path = '/mnt/c/Users/13669/Downloads/alipay_record_20231127_092126.csv'
header_keyword = '交易时间'
csv_data = _read_csv_with_header(csv_file_path, header_keyword)

for row in csv_data[1:]:
    print(row)
