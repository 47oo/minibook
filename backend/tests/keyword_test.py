import unittest
from db.database import SessionLocal
from repositories.keyword_repository import *

session =  SessionLocal()

class TestCreateKeywordMapping(unittest.TestCase):
    def setUp(self):
        # 设置测试环境准备操作，例如创建数据库表等
        pass
    
    def tearDown(self):
        # 清理测试环境，例如删除数据库表等
        pass
    
    def test_create_keyword_mapping(self):
        # 准备测试数据
        keyword = "test"
        transaction_type = "deposit"
        transaction_category = "credit"
        user_id = 1
        
        # 执行函数
        created_mapping = create_keyword_mapping(session, keyword, transaction_type, transaction_category, user_id)
        
        # 验证结果
        self.assertIsNotNone(created_mapping)
        self.assertEqual(created_mapping.keyword, keyword)
        self.assertEqual(created_mapping.transaction_type, transaction_type)
        self.assertEqual(created_mapping.transaction_category, transaction_category)
        self.assertEqual(created_mapping.user_id, user_id)
        self.assertTrue(session.query(KeywordMapping).filter(KeywordMapping.keyword == keyword).count() == 1)
        
        # 清理测试环境

class TestDeleteKeywordMapping(unittest.TestCase):
    def setUp(self):
        # 设置测试环境，例如创建数据库表和记录
        pass

    def tearDown(self):
        # 清理测试环境，例如删除数据库表和记录
        pass

    def test_delete_existing_keyword_mapping(self):
        # 创建一个已存在的关键字映射记录
        session = SessionLocal()
        # 调用被测试函数
        result = delete_keyword_mapping(session, 1)

        # 断言被测试函数的返回值和关键字映射记录的状态
        self.assertEqual(result.id, 1)
        session.close()



if __name__ == "__main__":
    unittest.main()

