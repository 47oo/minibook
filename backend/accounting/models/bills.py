# bill_model.py

from .base import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Bill(Base):
    __tablename__ = 'bills'

    id = Column(Integer, primary_key=True, index=True)
    transaction_time = Column(DateTime, nullable=False)
    transaction_type = Column(String, nullable=False)  # 交易类型，例如购物、租金等,一笔交易只能设置一个类型
    counterparty = Column(String, nullable=False)  # 交易方
    description = Column(String)  # 商品说明
    transaction_amount = Column(Float, nullable=False)  # 交易金额
    transaction_category = Column(String)  # 收支类型，例如支出、收入
    funding_source = Column(String)  # 资金来源，例如银行卡、现金等

    # 外键关联到用户表
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='bills')
