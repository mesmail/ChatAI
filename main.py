import os
from chat_with_rag import ChatWithRAG

API_KEY = "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"

chat_system = ChatWithRAG(API_KEY)

# إضافة مستندات إلى النظام
chat_system.add_document("Artificial intelligence is the simulation of human intelligence in machines.")

# تجربة النظام
query = "What is artificial intelligence?"
response = chat_system.chat(query)
print(response)
# Output: Artificial intelligence is the simulation of human intelligence in machines.