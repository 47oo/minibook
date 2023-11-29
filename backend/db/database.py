from models.base import Base
from models.user_model import User
from models.bill_model import Bill
from models.keyword_mapping_model import KeywordMapping
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


