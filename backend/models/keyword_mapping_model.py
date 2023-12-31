# keyword_mapping_model.py

from .base import Base
from sqlalchemy import Column, Integer, String

class KeywordMapping(Base):
    __tablename__ = 'keyword_mapping'

    id = Column(Integer, primary_key=True)
    keyword = Column(String, unique=True, nullable=False)  # 关键字
    transaction_type = Column(String, nullable=False)  # 交易类型
    transaction_category = Column(String, nullable=False)  # 收支类型
    
    user_id = Column(Integer, nullable=False) # 创建该关键字的用户名称
