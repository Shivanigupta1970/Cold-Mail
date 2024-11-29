from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    groq_api_key="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"
)

response=llm.invoke('the forst person land on moon')
print(response)