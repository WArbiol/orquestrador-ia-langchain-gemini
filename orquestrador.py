import os
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool, tool
from langchain import hub

from langchain_community.tools import DuckDuckGoSearchRun
from langchain.chains.llm_math.base import LLMMathChain

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0) # preciso (entre 0 e 1)

# Ferramenta 1: Pesquisa Web
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="Web Search",
    func=search.run,
    description="Use para pesquisar informações recentes na internet. Forneça uma query de busca objetiva."
)

# Ferramenta 2: Calculadora
math_chain = LLMMathChain.from_llm(llm)
calculator_tool = Tool(
    name="Calculator",
    func=math_chain.run,
    description="Use para resolver qualquer problema ou cálculo matemático. Ex: 'quanto é 5 vezes 7?'"
)

# Ferramenta 3: Tradutor
@tool
def translate_text(query: str) -> str:
    """
    Traduz um texto para um idioma de destino.
    O input para esta ferramenta deve ser uma string no formato:
    'texto para traduzir' PARA 'idioma de destino'.
    Por exemplo: 'hello world' PARA 'português'.
    """
    prompt = f"Traduza o seguinte texto: {query}"
    response = llm.invoke(prompt)
    return response.content

# Ferramenta 4: Análise de Sentimento
@tool
def analyze_sentiment(text: str) -> str:
    """Analisa o sentimento de um texto, retornando Positivo, Negativo ou Neutro."""
    prompt = f"Analise o sentimento do seguinte texto e responda apenas com 'Positivo', 'Negativo' ou 'Neutro': '{text}'"
    response = llm.invoke(prompt)
    return response.content

# -- AGENTE --
tools = [search_tool, calculator_tool, translate_text, analyze_sentiment]
prompt = hub.pull("hwchase17/react") # prompt que instrui como usar o agente

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors=True, 
    warnings = False,
    max_iterations=10
)

# --- CONVERSA INTERATIVO ---
print("\n✅ Orquestrador de IA pronto! Faça suas perguntas abaixo.")
print("   Digite 'sair' ou 'exit' para terminar o programa.")
print("-" * 60)
while True:
    user_question = input("Você: ")
    if user_question.lower() in ["sair", "exit", "quit"]:
        print("\nAté logo!")
        break

    if user_question:
        try:
            response = agent_executor.invoke({
                "input": user_question
            })
            print("\nIA:", response["output"], "\n")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            print("Por favor, tente novamente.")
    else:
        print()