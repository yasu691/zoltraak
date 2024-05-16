import os
import openai
from zoltraak import settings

def generate_response(model, prompt, max_tokens, temperature):
    """
    OpenAI APIを使用してプロンプトに対する応答を生成する関数。

    Args:
        prompt (str): 応答を生成するためのプロンプト。

    Returns:
        str: 生成された応答テキスト。
    """
    
    # OpenAIのAPIキーを設定
    client = openai.OpenAI(api_key = os.environ.get("OPEN_AI_API_KEY"))  # 環境変数からAPI keyを取得

    # モデルエンジンの選択
    model_engine = "gpt-3.5-turbo-16k"

    print(prompt)

    # APIリクエストのパラメータ設定
    response = client.chat.completions.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4096,
        n=1,
        temperature=temperature,
    )


    print(response)
    
    return response.choices[0].message

if __name__=="main":
    print(generate_response("", "hello", 4096, 0.3))
