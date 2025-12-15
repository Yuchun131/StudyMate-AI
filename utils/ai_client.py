# utils/ai_client.py
import requests
import config

def ask_ai(prompt):
    """向DeepSeek AI发送请求并返回回复"""
    api_key = config.DEEPSEEK_API_KEY
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"请求出错：{e}"