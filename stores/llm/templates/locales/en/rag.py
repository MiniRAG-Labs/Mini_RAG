from string import Template

#### RAG PROMPTS ####

#### System ####

system_prompt = Template("\n".join([
    "You are a helpful AI assistant that answers questions based on provided documents.",
    "Your task is to generate accurate and informative responses using ONLY the information from the documents.",
    "If the documents contain relevant information, provide a clear and comprehensive answer.",
    "If the documents do not contain enough information to answer the question, politely explain what information is missing.",
    "Always maintain the same language as the user's question.",
    "Be professional, accurate, and concise.",
]))

#### Document ####
document_prompt = Template(
    "\n".join([
        "Document $doc_num:",
        "$chunk_text",
        "",
    ])
)

#### Footer ####
footer_prompt = Template("\n".join([
    "",
    "Based on the documents above, please answer the following question:",
    "",
    "Question: $query",
    "",
    "Provide a clear, accurate answer using only the information from the documents.",
    "",
    "Answer:",
]))