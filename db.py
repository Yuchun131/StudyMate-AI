import sqlite3
import os

# SQLite数据库就是一个本地文件
DB_FILE = 'studymate.db'

def get_db_connection():
    """创建并返回一个SQLite数据库连接"""
    # 连接到本地文件，如果文件不存在会自动创建
    connection = sqlite3.connect(DB_FILE)
    # 设置返回格式为字典，方便通过列名取数据
    connection.row_factory = sqlite3.Row
    return connection

def init_database():
    """
    初始化SQLite数据库和表。
    注意：此函数应在应用启动时仅调用一次。
    """
    print("🔄 正在初始化SQLite数据库...")
    
    # SQLite不需要"创建数据库"这一步，直接连接文件就会创建。
    # 我们只需要确保表存在。
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        # SQLite的建表语句（注意与MySQL语法的区别）
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS conversation_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- SQLite用 INTEGER AUTOINCREMENT
            user_question TEXT NOT NULL,
            ai_answer TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- SQLite支持这个默认值
        );
        """
        cursor.execute(create_table_sql)
        conn.commit()
        print("✅ 数据表 'conversation_history' 已就绪。")
    except Exception as e:
        print(f"❌ 创建数据表时出错: {e}")
        raise
    finally:
        conn.close()
    
    print("🎉 SQLite数据库初始化完成！")

def save_conversation(question, answer):
    """将一次问答对话保存到数据库"""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        # SQLite 使用 ? 作为参数占位符
        sql = "INSERT INTO conversation_history (user_question, ai_answer) VALUES (?, ?)"
        cursor.execute(sql, (question, answer))
        conn.commit()
        print(f"💾 对话已保存: {question[:30]}...")  # 只打印前30个字符
        return True
    except Exception as e:
        print(f"❌ 保存对话时出错: {e}")
        return False
    finally:
        conn.close()

def get_all_conversations(limit=50):
    """从记忆仓库里取出最近的对话历史"""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        # 按时间倒序排列，获取最近的记录
        sql = """SELECT * FROM conversation_history 
               ORDER BY created_at DESC 
               LIMIT ?"""
        cursor.execute(sql, (limit,))
        # fetchall() 获取所有结果行
        conversations = cursor.fetchall()
        print(f"📜 从记忆仓库加载了 {len(conversations)} 条历史记录。")
        return conversations
    except Exception as e:
        print(f"❌ 加载历史记录失败: {e}")
        return []
    finally:
        conn.close()

# 测试代码：当直接运行此脚本时，会执行初始化
if __name__ == '__main__':
    init_database()
    # 可选：测试一下保存功能
    # save_conversation("测试问题", "测试回答")
    if __name__ == '__main__':
     init_database()
    # 临时添加：插入几条测试数据
if __name__ == '__main__':
    init_database()
    # 临时添加：插入几条测试数据
    save_conversation('第一个测试问题', '这是第一条测试回答')
    save_conversation('第二个测试问题', '这是第二条测试回答')
    save_conversation('Python装饰器是什么？', '装饰器是...')