import os
from openai import AzureOpenAI
from pinecone import Pinecone
from core_logic import retrieve, prompt_with_context_builder, generate_answer

# Configuration (Best practice: use environment variables)
EMB_MODEL = "text-embedding-3-small"
CHAT_DEPLOYMENT = "gpt-5.2-chat-2"

client = AzureOpenAI(
    api_key=os.getenv('AZURE_API'),
    azure_endpoint=os.getenv('AZURE_ENDPOINT'),
    api_version="2024-12-01-preview"
)

pc = Pinecone(api_key=os.getenv('PINECONE'))
index = pc.Index('youtube-rag-data')

def rag_pipeline(query):
    # 1. Retrieve
    docs, sources = retrieve(query, 3, 'youtube-data', index, client, EMB_MODEL)
    
    # 2. Build Prompt
    prompt = prompt_with_context_builder(query, docs)
    
    # 3. Generate
    answer = generate_answer(client, prompt, CHAT_DEPLOYMENT)
    
    # Format Output
    full_response = f"{answer}\n\nSources:"
    for title, url in sources:
        full_response += f"\n- {title}: {url}"
    return full_response

if __name__ == "__main__":
    user_query = "How to build next-level Q&A with OpenAI?"
    print(rag_pipeline(user_query))