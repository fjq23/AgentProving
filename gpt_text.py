import openai
import httpx

from prompt import TASK_DESCRIPTION


class GPT4Model: # 使用US-A节点
    def __init__(self):
        self.system_prompt = "You are an assistant with strong logical thinking skills, adept at learning and helping me solve mathematical problems."

    def call_gpt_api(self, prompt):
        prompt_input = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]
        try:
            with httpx.Client(timeout=httpx.Timeout(60.0)) as client:
                response = client.post(
                    url=f"{openai.api_base}/chat/completions",
                    headers={
                        "Authorization": f"Bearer {openai.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "gpt-4o-2024-05-13",
                        "messages": prompt_input,
                        "max_tokens": 1024,
                        "temperature": 0,
                    },
                )
            response.raise_for_status()
            response_json = response.json()
            return [choice["message"]["content"] for choice in response_json["choices"]][0]
        except Exception as e:
            print(f"API调用失败: {e}")
            print(response.json())
            return ""
    def generate_solution(self, formula):

        self.call_gpt_api(TASK_DESCRIPTION)

# gpt = GPT4Model()
# reply = gpt.call_gpt_api("hi")
# print(reply)