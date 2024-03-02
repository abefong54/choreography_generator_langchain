from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from dotenv import load_dotenv

load_dotenv()


def generate_pet_name(user_dance_type, user_student_level):
    llm = OpenAI(temperature=0)
    # temperature = 0, less creative, very safe, no risks
    # temperature = 1, more creative, maybe wrong,


    # PromptTemplates
    # Make it easier to generate prompts so we don’t have to keep asking a different prompt every time. 
	# Repurpose prompts, variables in the prompt.
    # prompt_string = "I have a {animal_type} and I want a cool name for it. It is {pet_color}. Suggest me five cool names for my pet"
    prompt_string = "I am a {user_dance_type} teacher and I want a quick choreo pattern to teach for my class. It is for {user_student_level} level dancers. Suggest me five cool patterns I can teach in an hour."
    prompt_template_name = PromptTemplate(
        input_variables=['user_dance_type', 'user_student_level'],
        template=prompt_string
    )
    
    # Chains
    # helps us connect components together.
    # in our case, the above prompt templates and llms below
    # output key is result,instead of a text, it'll store the generated values into this key 'pet_name'
    name_chain = LLMChain(llm=llm,prompt=prompt_template_name,output_key="choreo_results")

    response = name_chain({'user_dance_type':user_dance_type, 'user_student_level':user_student_level}) # pass in the variable to the chain
    return response


# def langchain_agent():
#     llm = OpenAI(temperature=0.5)

#     toolset = load_tools(["wikipedia", "llm-math"], llm = llm)

#     agent = initialize_agent(
#         tools=toolset,
#         llm=llm,
#         agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
#         verbose=True
#     )

#     result = agent.run(
#        "Use wikipedia, What is the average age of a dog? Then, Multiply the age by 3."
#     )
    
#     print(result)


# if __name__ == "__main__":
#     langchain_agent()