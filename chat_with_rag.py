from chat_model import ChatModel
from rag_system import RAGSystem

class ChatWithRAG:
    def __init__(self, api_key):
        self.chat_model = ChatModel(api_key)
        self.rag_system = RAGSystem(api_key)

    def add_document(self, text):
        """إضافة مستندات إلى النظام"""
        self.rag_system.add_document(text)

    def chat(self, query):
        """استرجاع معلومات من RAG إذا كانت ذات صلة، وإلا تنفيذ محادثة عادية."""
        relevant_texts = self.rag_system.search(query)
        if relevant_texts:
            context = " ".join(relevant_texts)
            query = f"Based on the following document, answer the question:\n{context}\n\nQuestion: {query}"
        return self.chat_model.generate_response(query)
