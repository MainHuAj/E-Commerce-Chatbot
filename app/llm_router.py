from groq import Groq
from dotenv import load_dotenv
load_dotenv()
client = Groq()

def route_query(query):
    prompt = f"""
    Classify the user query into one of:
    - faq
    - sql
    - other
    Do not give any explanation or preamble just faq or sql or other for example if the query is like "Do you accept cash payment " then reply with faq

    Query: {query}
    """

    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content.strip()

if __name__ == "__main__":
    query = "What is the refund policy"
    result = route_query(query)
    print(result)
