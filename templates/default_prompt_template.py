from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


default_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """ You are a helpful AI Assistant. Use the following context to help you answer the question: \n{context} """,
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)
