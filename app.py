# app.py - 总路由控制器
from flask import Flask, render_template, request

# 🧠 大脑：导入所有需要的核心部件
from flask import Flask, render_template, request# Web框架全家桶
from utils import ai_client# 我们的AI智慧核心
from db import init_database, save_conversation# 项目记忆仓库的管理员

# 🏗️ 骨架：搭建Flask应用的主框架
app = Flask(__name__)
app.config.from_pyfile('config.py')                 # 加载秘密配置

# 💾 记忆唤醒：启动时，确保记忆仓库准备就绪
init_database()
print("✅ Flask应用已连接至数据库。")

# 导入配置（后续可以从这里读取密钥等）
app.config.from_pyfile('config.py')

# 主页：介绍StudyMate
@app.route('/')
def index():
    return render_template('index.html')

# 未来可以在这里添加更多路由，例如：
# @app.route('/plan/save', methods=['POST'])
# def save_plan():
#     pass

from utils import ai_client
# 新增：导入我们刚刚改造好的数据库模块
from db import init_database, save_conversation

@app.route('/history')
def show_history():
    """历史记录陈列室：展示所有记忆"""
    # 调用我们刚写的函数，获取历史记录
    from db import get_all_conversations
    chats = get_all_conversations()
    
    # 将每条记录从SQLite的Row对象转为普通字典，方便模板使用
    history_list = []
    for chat in chats:
        history_list.append({
            'id': chat['id'],
            'question': chat['user_question'],
            'answer': chat['ai_answer'],
            'time': chat['created_at']  # 这里返回的是原始时间戳，可以后续格式化
        })
    
    # 把历史记录列表传给一个新的网页模板
    return render_template('history.html', histories=history_list)

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form.get('question', '').strip()
    if not user_input:
        return render_template('index.html', error="⚠️ 问题不能为空哦！")

    answer_text = ai_client.ask_ai(user_input)  # 这是你原来的AI调用

    # 新增：将问答对话保存到数据库
    save_conversation(user_input, answer_text)

    # 原来的返回语句保持不变
    return render_template('index.html',
                           question=user_input,
                           answer=answer_text)

if __name__ == '__main__':
    app.run(debug=True)