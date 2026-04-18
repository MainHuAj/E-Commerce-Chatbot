# 🛍️ E-Commerce Chatbot — Women's Sports Shoes

An AI-powered chatbot for a women's sports shoes e-commerce platform. Uses LLM-based semantic routing to classify user queries and respond intelligently — either answering policy-related FAQs or querying a product database using natural language.

---

## 🚀 Live Demo

👉 [Try it on Streamlit Cloud](https://e-commerce-chatbot-mzd7c4vmtgcwhhvh8sigba.streamlit.app)

> **Note:** This chatbot is specialized for **women's sports shoes** only. Product search outside this category may not return results.

---

## 🧠 How It Works

User queries are routed through an **LLM-based router** (Groq + LLaMA 3.3 70B) into one of three categories:

| Route | Description |
|-------|-------------|
| `faq` | Policy questions — returns, refunds, payments, tracking |
| `sql` | Product queries — brand, price, rating, discount, size filters |
| `other` | Out-of-scope queries — handled gracefully |

### FAQ Pipeline
1. Query hits the **LLM Router** → classified as `faq`
2. ChromaDB performs **vector similarity search** on FAQ data
3. Top 2 relevant Q&A pairs are retrieved as context
4. Groq LLM generates a natural language answer grounded in that context

### Product Search Pipeline
1. Query hits the **LLM Router** → classified as `sql`
2. Groq LLM converts natural language to a **SQL query**
3. Query runs against a **SQLite product database**
4. Results are summarized in plain English by a second LLM call

---

## 🗂️ Project Structure

```
e-commerce-chatbot/
├── app/
│   ├── main.py              # Streamlit UI and app entry point
│   ├── llm_router.py        # LLM-based semantic router
│   ├── faq.py               # ChromaDB ingestion + FAQ chain
│   ├── sql.py               # Text-to-SQL + data comprehension chain
│   ├── requirements.txt     # Project dependencies
│   └── resources/
│       ├── faq_data.csv     # FAQ question-answer pairs
│       └── db.sqlite        # Product database (women's sports shoes)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| UI | Streamlit |
| LLM | Groq (LLaMA 3.3 70B) |
| Vector DB | ChromaDB (in-memory) |
| Embeddings | all-MiniLM-L6-v2 via ONNX |
| Product DB | SQLite |
| Data | Pandas |

---

## ⚙️ Setup & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/MainHuAj/E-Commerce-Chatbot
cd e-commerce-chatbot/app
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file inside the `app/` folder:
```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 5. Run the app
```bash
streamlit run main.py
```

---

## 💬 Example Queries

**FAQ queries:**
- "What is your return policy?"
- "How long does a refund take?"
- "What payment methods do you accept?"

**Product queries:**
- "Show me top rated Puma shoes"
- "Give me Nike shoes under Rs 3000"
- "Puma shoes with rating above 4.5 and discount more than 30%"

---

## 📦 Dependencies

```
chromadb==1.5.7
groq==1.1.2
pandas==3.0.2
python-dotenv==1.0.1
streamlit==1.56.0
```

---

## ⚠️ Limitations

- Product database contains **women's sports shoes only** — queries for other categories will not return results
- Powered by Groq's free tier — back-to-back queries may occasionally hit rate limits (resets every minute)
- ChromaDB runs **in-memory** — FAQ data is re-ingested on cold starts

---

## 🙋 Author

**Abhinav Bhatera** — Final year B.Tech CS student | ML & AI enthusiast  
📺 [Curious Sapien](https://youtube.com/@curioussapien) — documenting the ML learning journey
