from sqlalchemy.orm import Session
from typing import List
from models.keyword_mapping_model import KeywordMapping


def create_keyword_mapping(session: Session, km: KeywordMapping):
    """
    创建一个新的关键字映射记录。
    """
    session.add(km)
    session.commit()
def create_keyword_mappings(session: Session, kms: List[KeywordMapping]):
    """
    创建一个新的关键字映射记录。
    """
    for km in kms:
        session.add(km)
    session.commit()

def get_keyword_mapping2dict(session: Session):
    kwsdict = {}
    kws = session.query(KeywordMapping).all()
    for kw in kws:
        kwsdict[kw.keyword] ={
            "transaction_type": kw.transaction_type,
            "transaction_category": kw.transaction_category,
        }
    return kwsdict


def get_keyword_mapping_by_id(session: Session, keyword_mapping_id: int):
    """
    通过ID检索关键字映射记录。
    """
    return session.query(KeywordMapping).filter(KeywordMapping.id == keyword_mapping_id).first()

def update_keyword_mapping(session: Session, keyword_mapping_id: int, new_data: dict):
    """
    更新关键字映射记录。
    """
    keyword_mapping = session.query(KeywordMapping).filter(KeywordMapping.id == keyword_mapping_id).first()
    if keyword_mapping:
        for key, value in new_data.items():
            setattr(keyword_mapping, key, value)
        session.commit()
        return keyword_mapping
    return None

def delete_keyword_mapping(session: Session, keyword_mapping_id: int):
    """
    通过ID删除关键字映射记录。
    """
    keyword_mapping = session.query(KeywordMapping).filter(KeywordMapping.id == keyword_mapping_id).first()
    if keyword_mapping:
        session.delete(keyword_mapping)
        session.commit()
        return keyword_mapping
    return None

def init_data(session: Session):
    # Check if there is any data in the keyword_mapping table
    existing_data = session.query(KeywordMapping).first()
    default_data = [
        {
            "keyword": "超市",
            "transaction_type": "超市采购",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "餐厅",
            "transaction_type": "餐饮",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "食堂",
            "transaction_type": "餐饮",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "保险",
            "transaction_type": "保险",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "高德",
            "transaction_type": "交通",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "美团",
            "transaction_type": "餐饮",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "充值",
            "transaction_type": "娱乐",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "暖宝宝",
            "transaction_type": "日用百货",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "收钱码",
            "transaction_type": "餐饮",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "肉饼",
            "transaction_type": "餐饮",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "湿厕巾",
            "transaction_type": "日用百货",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "垃圾袋",
            "transaction_type": "日用百货",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "小米",
            "transaction_type": "数码电器",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "纸巾",
            "transaction_type": "日用百货",
            "transaction_category": "支出",
            "user_id": 0
        },
         {
            "keyword": "洗发水",
            "transaction_type": "日用百货",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "舒肤佳",
            "transaction_type": "日用百货",
            "transaction_category": "支出",
            "user_id": 0
        },
        {
            "keyword": "手套",
            "transaction_type": "日用百货",
            "transaction_category": "支出",
            "user_id": 0
        }
    ]

    if not existing_data:
        # If there is no data, create default data
        for data in default_data:
            new_mapping = KeywordMapping(
                keyword=data["keyword"],
                transaction_type=data["transaction_type"],
                transaction_category=data["transaction_category"],
                user_id=data["user_id"]
            )

            # Add the default data to the database
            session.add(new_mapping)
        session.commit()
