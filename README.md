# 🤖 Orquestrador de Ferramentas IA com LangChain e Gemini

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-0.2-orange?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Gemini_API-1.5-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Um projeto de aprendizado para criar um agente de IA simples capaz de orquestrar múltiplas ferramentas como busca na web, calculadora e tradução, utilizando o poder do LangChain e da API do Google Gemini.

---

### 🌟 Demonstração em GIF

![Demo GIF](https-link-para-seu-gif-aqui.gif)

---

### ✨ Features

- **Interativo:** Converse com o agente diretamente do seu terminal.
- **Multi-Ferramentas:** O agente pode decidir quando e como usar:
  - 🔎 **Busca na Web:** Para perguntas sobre eventos atuais e informações gerais.
  - 🧮 **Calculadora:** Para resolver operações matemáticas com precisão.
  - 🌐 **Tradutor:** Para traduzir textos entre idiomas.
  - 🤔 **Análise de Sentimento:** Para identificar o tom de uma frase.
- **Chain of Thought:** Veja o "raciocínio" do agente em tempo real, graças ao `verbose=True`.
- **Fácil de Configurar:** Pronto para rodar com apenas alguns comandos.

---

### 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Framework de IA:** [LangChain](https://www.langchain.com/)
- **Modelo de Linguagem (LLM):** Google Gemini 1.5 Flash
- **Ferramentas:** DuckDuckGo (via `ddgs`), LLMMathChain

---

### 🚀 Como Usar

Siga os passos abaixo para executar o projeto localmente.

#### Pré-requisitos

- [Python 3.10 ou superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads/)
- Uma chave de API do [Google AI Studio](https://aistudio.google.com/app/apikey)

#### Passos para Instalação

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/SEU_USUARIO/orquestrador-ia-langchain-gemini.git](https://github.com/SEU_USUARIO/orquestrador-ia-langchain-gemini.git)
    cd orquestrador-ia-langchain-gemini
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure suas credenciais:**

    - Renomeie o arquivo `.env.example` para `.env`.
    - Abra o arquivo `.env` e substitua o placeholder pela sua chave de API do Google.

    ```
    GOOGLE_API_KEY="SUA_CHAVE_DE_API_DO_GOOGLE_VEM_AQUI"
    ```

5.  **Execute o orquestrador!**
    ```bash
    python orquestrador_interativo.py
    ```

---

### 💬 Exemplo de Interação

```
✅ Orquestrador de IA pronto! Faça suas perguntas abaixo.
   Digite 'sair' ou 'exit' para terminar o programa.
------------------------------------------------------------
Você: Olá! Qual a capital do Japão e como se diz "obrigado" em japonês?

> Entering new AgentExecutor chain...
Thought: O usuário tem duas perguntas. Uma sobre a capital do Japão e outra sobre uma tradução. Vou começar com a busca na web para a capital.
Action: Web Search
Action Input: "capital do Japão"
Observation: Tóquio
Thought: A capital é Tóquio. Agora vou traduzir "obrigado" para japonês.
Action: translate_text
Action Input: 'obrigado' PARA 'japonês'
Observation: ありがとう (Arigatō)
Thought: Eu tenho as duas partes da resposta. Posso finalizar.
Action: Finish
Final Answer: A capital do Japão é Tóquio. "Obrigado" em japonês se diz ありがとう (Arigatō).

> Finished chain.

Orquestrador IA: A capital do Japão é Tóquio. "Obrigado" em japonês se diz ありがとう (Arigatō).

Você: sair

Até logo!
```

---

### 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
