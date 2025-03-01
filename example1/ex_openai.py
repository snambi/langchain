from secret_key import openapi_key
from langchain_openai import OpenAI

import os

os.environ['OPENAI_API_KEY'] = openapi_key

#print(openapi_key)
print(os.environ['OPENAI_API_KEY'])

llm = OpenAI(temperature=0.6)
name = llm("Suggest a fancy name for an indian restaurant");
print(name)