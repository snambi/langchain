from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
import json

def generate_restaurant_name(cuisine:str):

    model = OllamaLLM(model="llama3.2:1b", temperature=0.6)

    prompt_template_name2 = PromptTemplate(
        input_variables= ['cuisine'],
        template = "I want to open an restaurent for {cuisine} food. Suggest a fancy name. Return only one name without any other text"
    )

    prompt_template_name2.format(cuisine="Mexican")

    name_chain2 = LLMChain(llm=model, prompt=prompt_template_name2, output_key="restaurant_name")

    prompt_template_items2 = PromptTemplate(
        input_variables= ['restaurant_name'],
        template = "Suggest some menu items for {restaurant_name}. Return it as a comma separated list without any metadata"
    )

    food_items_chain2 = LLMChain(llm=model, prompt=prompt_template_items2, output_key="menu_items")

    chain = SequentialChain(
        chains = [name_chain2, food_items_chain2],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name', 'menu_items' ]
    )

    out_response = chain.invoke({'cuisine':cuisine})

    print("response: "+ str(out_response))

    return out_response


if __name__ == "__main__":
    output = generate_restaurant_name("Tibetian")
    print("Cuisine: "+ output['cuisine'])
    print("Name: " + output['restaurant_name'])
    print("Menu: " + output['menu_items'])