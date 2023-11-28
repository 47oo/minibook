import os

class MiniBook:
    def __init__(self, db_name):
        self.db_name = db_name

    def abs_db_path(self):
        # 获取当前脚本的目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        app_dir = os.path.dirname(parent_dir)

        # 构建相对路径
        relative_path = f"data/sqlite_db/{self.db_name}"

        # 获取绝对路径
        absolute_path = os.path.join(app_dir, relative_path)

        return absolute_path

mini_book = MiniBook("minibook.sqlite")

