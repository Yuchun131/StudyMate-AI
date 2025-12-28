import pymysql.cursors
import os
from dotenv import load_dotenv

# 1. 加载 .env 文件中的环境变量
load_dotenv()

def get_db_connection():
    """创建并返回一个数据库连接"""
    connection = pymysql.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        port=int(os.getenv('DB_PORT', 3306)),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'studymate_db'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def init_database():
    """
    初始化数据库和表。
    注意：此函数应在应用启动时仅调用一次。
    """
    print("正在初始化数据库...")
    
    # 第一步：连接到MySQL服务器（不指定具体数据库），为了创建数据库
    conn_for_create = pymysql.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        port=int(os.getenv('DB_PORT', 3306)),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        charset='utf8mb4'
    )
    
    try:
        with conn_for_create.cursor() as cursor:
            # 创建数据库（如果不存在）
            db_name = os.getenv('DB_NAME', 'studymate_db')
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
            print(f"✅ 数据库 '{db_name}' 已就绪。")
        conn_for_create.commit()
    except Exception as e:
        print(f"❌ 创建数据库时出错: {e}")
        raise
    finally:
        conn_for_create.close()
    
    # 第二步：连接到我们刚创建/确认存在的具体数据库，为了创建表
    conn_for_table = get_db_connection()
    try:
        with conn_for_table.cursor() as cursor:
            # 创建对话历史表 (就是你设计的 conversation_history)
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS conversation_history (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_question TEXT NOT NULL,
                ai_answer TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """
            cursor.execute(create_table_sql)
            print("✅ 数据表 'conversation_history' 已就绪。")
        conn_for_table.commit()
    except Exception as e:
        print(f"❌ 创建数据表时出错: {e}")
        raise
    finally:
        conn_for_table.close()
    
    print("🎉 数据库初始化完成！")

# 测试代码：当直接运行此脚本时，会执行初始化
if __name__ == '__main__':
    init_database()