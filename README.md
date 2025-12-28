# StudyMate-AI: 个人智能学习伙伴

## 🎯 项目概述
一个基于Python Flask与AI大模型开发的智能学习计划生成器。旨在通过AI技术，为自学编程者提供个性化的学习路径规划。

## 🛠️ 技术栈
- **后端**: Python 3.14, Flask
- **AI服务**: DeepSeek API
- **前端**: HTML (Jinja2模板), CSS
- **开发工具**: Git, VSCode, Windows PowerShell
- **项目管理**: 虚拟环境 (venv), 模块化设计

## 📁 项目结构
```
StudyMate-AI/
├── app.py # Flask应用主入口与路由控制
├── config.py # 配置文件（API密钥等，已.gitignore）
├── requirements.txt # Python依赖包列表
├── .gitignore # 排除配置文件等
├── README.md # 项目说明文档
│
├── static/ # 静态资源（CSS、JS）
│ └── style.css
├── templates/ # HTML模板文件
│ ├── base.html
│ ├── index.html
│ └── generator.html
└── utils/ # 核心工具模块
├── init.py
└── ai_client.py
```

## 🚀 如何运行 (本地开发)
1.  **克隆仓库**:
    ```bash
    git clone https://github.com/Yuchun131/StudyMate-AI.git
    cd StudyMate-AI
    ```

2.  **创建并激活虚拟环境** (Windows):
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **安装依赖**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **配置API密钥**:
    - 在项目根目录创建 `config.py` 文件
    - 添加内容: `DEEPSEEK_API_KEY = '你的实际密钥'`
    - **确保`config.py`已列入`.gitignore`**

5.  **启动开发服务器**:
    ```bash
    python app.py
    ```
    在浏览器访问 [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📖 开发日志与思考
### 2025年11月20日 - 项目初始化
- 目标：完成从零开始的Python Web开发环境搭建。
- 动作：成功配置Python、Flask、Git，并理解虚拟环境的重要性。
- 难点/解决：PowerShell中无法直接运行Python代码，需创建.py文件后执行。
- 思考：理解了“环境”是开发的第一步，也是排除最多错误的地方。

### 2025年11月25日 - 安全配置与项目骨架
- 目标：安全存储API密钥并建立可扩展的项目结构。
- 动作：采用`config.py + .gitignore`方案保护密钥；按MVC思想规划目录。
- 难点/解决：理解`__init__.py`的作用是让文件夹成为可导入的Python包。
- 思考：工程化不只是写代码，更是关于安全、维护和协作的规划。

### 2025年12月05日 - 实现核心AI功能连通
- 目标：完成AI API的首次成功调用。
- 动作：编写并测试`test_api.py`，验证了从本地到AI服务的完整链路。
- 思考：看到了将外部强大能力（AI）集成到自己应用中的实际效果，理解了API的价值。

### 2025年12月27日 - 增加数据持久化
目标：为应用添加数据库，保存对话历史。
动作：设计SQLite表结构，在 db.py 中实现数据保存与查询，并创建 /history 页面展示记录。
难点/解决：
智能引号导致语法错误：发现代码中混入中文弯引号，通过编辑器全局替换为英文直引号解决。

保存函数静默失败：因函数体代码被覆盖，补全 save_conversation 函数实现后正常。
思考：环境一致性（如引号编码）是隐蔽的坑；完成“输入-处理-存储-展示”的完整闭环，项目才真正可用。

## 后续计划
✅ 完成 `utils/ai_client.py` 模块，封装所有AI调用
✅ 设计并实现前端页面，实现用户与AI的简单交互
✅ 添加学习计划保存与查看功能 (已实现为【对话历史】)
⏳ 部署项目到公网
⏳ (新增) 为历史记录页面增加交互功能（如删除单条记录、关键词搜索）
⏳ (新增) 完善项目配置，便于在不同环境（开发/生产）中一键切换

## 📄 许可证
本项目为个人学习项目。