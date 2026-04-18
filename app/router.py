# not using it as it was not giving good results

from semantic_router import Route , SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    name = 'sentence-transformers/all-MiniLM-L6-v2'
)

faq = Route(
    name="faq",
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process refund?",
        "What happens if I receive a damaged product?",      # <-- covers defective
        "What do I do if my product is defective?",          # <-- direct match
        "Can I return a broken or faulty item?",
        "What is the policy for damaged goods?",
        "How do I report a defective product?"
    ]
)

sql = Route(
    name = "sql",
    utterances=[
        "I want to buy Nike shoes that have 50% discount",
        "Are there any shoes under Rs 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of Puma running shoes?"
    ]
)


router = SemanticRouter(encoder=encoder, routes=[faq, sql], auto_sync="local")
router.score_threshold = 0.3

