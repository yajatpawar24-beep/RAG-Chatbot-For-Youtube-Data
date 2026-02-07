import pandas as pd
import numpy as np
from uuid import uuid4

def run_ingestion(df, client, index, model_name, batch_limit=100):
    """Processes CSV and upserts embeddings to Pinecone."""
    for batch in np.array_split(df, len(df)/batch_limit):
        metadatas = [
            {
                'text_id': row['id'],
                'text': row['text'],
                'title': row['title'],
                'url': row['url'],
                'published': row['published']
            }
            for _, row in batch.iterrows()
        ]

        texts = batch['text'].tolist()
        ids = [str(uuid4()) for _ in range(len(texts))]

        response = client.embeddings.create(
            input=texts,
            model=model_name
        )

        embeds = [np.array(x.embedding) for x in response.data]

        index.upsert(
            vectors=zip(ids, embeds, metadatas),
            namespace='youtube-data'
        )
    print("Ingestion complete.")