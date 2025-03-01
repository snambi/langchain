import os

from langchain_core.prompts import PromptTemplate
#from langchain_community.llms.huggingface_hub import HuggingFaceHub
from langchain.chains.llm import LLMChain

os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'HF_API_KEY'

template = """Question: {question}

Answer: """
prompt = PromptTemplate(
        template=template,
    input_variables=['question']
)

# user question
question = "Which NFL team won the Super Bowl in the 2010 season?"

# initialize Hub LLM
hub_llm = HuggingFaceEndpoint(
        repo_id='google/flan-t5-xl',
        temperature='1e-10'
)

# create prompt template > LLM chain
llm_chain = LLMChain(
    prompt=prompt,
    llm=hub_llm
)

# ask the user question about NFL 2010
print(llm_chain.run(question))

