import os
from chat_with_rag import ChatWithRAG

API_KEY = "your_openai_api_key"

chat_system = ChatWithRAG(API_KEY)

# إضافة مستندات إلى النظام
chat_system.add_document("Artificial intelligence is the simulation of human intelligence in machines.")

# تجربة النظام
query = "What is artificial intelligence?"
response = chat_system.chat(query)
print(response)
# Output: Artificial intelligence is the simulation of human intelligence in machines.
