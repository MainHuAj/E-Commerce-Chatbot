from groq import Groq
from dotenv import load_dotenv
load_dotenv()
client = Groq()

def route_query(query):
    prompt = f"""
    Classify the user query into one of:
- faq: questions about policies, payments, refunds, returns, tracking, discounts
- sql: questions about finding, searching, or filtering products by brand, price, rating, discount, size, or any product attributes
- other: anything unrelated to the platform

Examples:
- "give me top rated puma shoes" → sql
- "show me nike shoes under 2000" → sql
- "what is your return policy" → faq
- "do you accept UPI" → faq
- "how are you" → other

Just reply with: faq, sql, or other. No explanation.

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
