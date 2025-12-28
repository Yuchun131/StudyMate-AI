# utils/ai_client.py
import requests
import config
import json

def ask_ai(prompt):
    """向智谱AI GLM-4.6模型发送请求并返回回复"""
    api_key = config.DEEPSEEK_API_KEY  # 虽然变量名没改，但值已是智谱Key

    # 智谱AI ChatCompletions API 的端点URL (这是通用地址)
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 数据体，模型名称指定为 'glm-4'
    data = {
        "model": "glm-4",  # 这是调用GLM-4.6系列模型的正确参数
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=30)
        response.raise_for_status()  # 检查请求是否成功

        # 解析智谱API返回的JSON数据
        result = response.json()
        # 正确的数据提取路径
        ai_reply = result['choices'][0]['message']['content']
        return ai_reply

    except requests.exceptions.RequestException as e:
        return f"网络请求错误：{e}"
    except (KeyError, json.JSONDecodeError) as e:
        return f"解析响应数据时出错，响应原文：{response.text}"
    except Exception as e:
        return f"发生未知错误：{e}"