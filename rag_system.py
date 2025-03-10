import openai
import faiss
import numpy as np

class RAGSystem:
    def __init__(self, api_key, dimension=1536):
        self.api_key = api_key
        self.dimension = dimension
        self.text_data = []
        self.embeddings = []
        
        # إنشاء FAISS Index
        self.index = faiss.IndexFlatL2(dimension)

    def embed_text(self, text):
        client = openai.OpenAI(api_key=self.api_key)  
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        return np.array(response.data[0].embedding, dtype=np.float32)

    def add_document(self, text):
        """إضافة مستند إلى النظام وتخزينه في FAISS."""
        embedding = self.embed_text(text)
        self.index.add(np.array([embedding]))  # إضافة التضمين إلى FAISS
        self.text_data.append(text)  # حفظ النص لاسترجاعه لاحقًا
        self.embeddings.append(embedding)

    def search(self, query, top_k=1):
        """ البحث عن نصوص ذات صلة باستعلام المستخدم. """
        query_embedding = self.embed_text(query)
        distances, indices = self.index.search(np.array([query_embedding]), top_k)
        return [self.text_data[i] for i in indices[0] if i < len(self.text_data)]
