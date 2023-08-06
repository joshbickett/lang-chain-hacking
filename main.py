from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

llm = OpenAI()
chat_model = ChatOpenAI()

text = "What would be a good company name for a company that makes colorful socks?"

t = llm.predict(text)
print("t", t)
# >> Feetful of Fun

t2 = chat_model.predict(text)
t2 = print("t2", t2)

# >> Socks O'Color
