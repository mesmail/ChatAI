import openai

class ChatModel:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)  # استخدام العميل الجديد

    def generate_response(self, prompt):
        response = self.client.chat.completions.create(  # استدعاء API وفق الإصدار الجديد
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content  # استخراج النص النهائي من الاستجابة
