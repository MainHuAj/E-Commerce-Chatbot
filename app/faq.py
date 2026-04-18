import pandas as pd
from pathlib import Path
import chromadb
# from chromadb.utils import embedding_functions
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
faqs_path = Path(__file__).parent/"resources/faq_data.csv"

client = chromadb.Client()
collection_name_faq ="faqs"
groq_client = Groq()
# ef = embedding_functions.SentenceTransformerEmbeddingFunction(
#     model_name = 'sentence-transformers/all-MiniLM-L6-v2'
# )
ef = DefaultEmbeddingFunction()

def ingest_faq_data(path):
    if collection_name_faq not in [c.name for c in  client.list_collections()]:
        print("Ingesting FAQ data into chromadb")
        collection = client.get_or_create_collection(
            name=collection_name_faq,
            embedding_function=ef
            )

        df = pd.read_csv(path)
        docs = df['question'].to_list()
        # metadatas are usually a list of dictionary or json objects
        metadata = [{"answer":ans } for ans in df['answer'].to_list()]
        ids = [f"id_{i}" for i in range(len(docs))]
        collection.add(
            documents=docs,
            metadatas=metadata,
            ids=ids
            )
        print("FAQ data successfully ingested in Chromadb")
    else:
        print(f"Collection already exist : {collection_name_faq}")

def get_relevant_qa(query):
    collection = client.get_collection(name = collection_name_faq)
    result = collection.query(
        query_texts=[query],
        n_results=2
    )
    return result

def faq_chain(query):
    result = get_relevant_qa(query)
    context = ''.join([r.get("answer") for r in result["metadatas"][0]])
    answer = generate_answer(query,context)
    return answer

def generate_answer(query,context):
    prompt = f'''Given the question and context below , generate the answer based on the context only.
    if you do not find the answer inside the context then say "I don't Know". Do not make things up.
    QUESTION:{query}
    CONTEXT : {context}
'''
    completion = groq_client.chat.completions.create(
    model=os.environ['GROQ_MODEL'],
    messages=[
      {
        "role": "user",
        "content": prompt
      }
    ],
    temperature=0.1,
)

       
    return completion.choices[0].message.content

if __name__ == "__main__":
    ingest_faq_data(faqs_path)
    # query = "What's your policy on defective product"
    query = "Do you accept cash as payment option"
    # print(get_relevant_qa(query))
    answer = faq_chain(query)
    print(answer)

    # print(faqs_path)
