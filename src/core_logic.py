import numpy as np
from uuid import uuid4

def retrieve(query, top_k, namespace, index, client, emb_model):
    """Retrieve relevant documents for a query."""
    query_response = client.embeddings.create(
        input=query,
        model=emb_model
    )
    query_emb = query_response.data[0].embedding

    docs = index.query(
        vector=query_emb,
        top_k=top_k,
        namespace=namespace,
        include_metadata=True
    )
    
    retrieved_docs = [doc['metadata']['text'] for doc in docs['matches']]
    sources = [(doc['metadata']['title'], doc['metadata']['url']) for doc in docs['matches']]
    return retrieved_docs, sources

def prompt_with_context_builder(query, docs):
    """Build a prompt with retrieved context."""
    delim = '\n\n--\n\n'
    prompt_start = 'Answer the question based on the context below. \n\nContext:\n'
    prompt_end = f'\n\nQuestion: {query}\nAnswer:'
    return prompt_start + delim.join(docs) + prompt_end

def generate_answer(client, prompt, chat_model):
    """Generate answer using LLM with retrieved context."""
    sys_prompt = "You are a helpful assistant that always answers questions"
    res = client.chat.completions.create(
        model=chat_model,
        messages=[
            {'role': 'system', 'content': sys_prompt},
            {'role': 'user', 'content': prompt}
        ]
    )
    return res.choices[0].message.content.strip()