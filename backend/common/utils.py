import pyzipper

def extract_password_protected_zip(zip_file_path, extract_to_path, password = None):
    """
    解压带密码的 ZIP 文件

    参数:
    - zip_file_path: ZIP 文件的路径
    - extract_to_path: 解压目标路径
    - password: ZIP 文件密码
    """
    with pyzipper.AESZipFile(zip_file_path, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(password)
        zipf.extractall(extract_to_path)

# 示例用法
zip_file_path = 'path/to/your/protected_file.zip'
extract_to_path = 'path/to/extract/location'
password = 'your_password'

extract_password_protected_zip(zip_file_path, extract_to_path, password)
