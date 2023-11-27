from models.base import Base
from config.minibook import mini_book
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建数据库引擎
DATABASE_URL = f"sqlite:///{mini_book.abs_db_path()}"
engine = create_engine(DATABASE_URL)

# 创建表
Base.metadata.create_all(bind=engine)
# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建数据库会话
db = SessionLocal()

# 现在可以使用 db 对象执行数据库操作
# ...

# 记得在最后关闭数据库会话
db.close()

