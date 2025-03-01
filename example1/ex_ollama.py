from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain.chains.llm import LLMChain

template = """Question: {question}
Answer: Let's think step by step.
"""

# prompt = ChatPromptTemplate.from_template(template)

prompt_template_name = PromptTemplate(
    input_variables= ['cuisine'],
    template = "I want to open an restaurant for {cuisine} food. Suggest a fancy name."
)

prompt_template_name.format(cuisine="Italian")

model = OllamaLLM(model="llama3.1:8b")

chain = LLMChain(llm=model, prompt=prompt_template_name)

chain.run("mexican")
#chain = prompt | model



