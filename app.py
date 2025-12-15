# app.py - 总路由控制器
from flask import Flask, render_template, request

app = Flask(__name__)

# 导入配置（后续可以从这里读取密钥等）
app.config.from_pyfile('config.py')

# 主页：介绍StudyMate
@app.route('/')
def index():
    return render_template('index.html')

# AI学习计划生成器页面
@app.route('/generate')
def generator_page():
    return render_template('generator.html')

# 未来可以在这里添加更多路由，例如：
# @app.route('/plan/save', methods=['POST'])
# def save_plan():
#     pass

from utils import ai_client

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form.get('question', '')
    if not user_input:
        return "请输入问题。"
    answer = ai_client.ask_ai(user_input)
    return render_template('generator.html', question=user_input, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)