# O que é o Ollama?

O **Ollama** é um software que permite **rodar modelos de Inteligência Artificial (LLMs)** diretamente no seu computador (**local/offline**), funcionando como um “ChatGPT local”, usando **CPU ou GPU**.

---

### Para que ele serve?

Com o Ollama você consegue:

- **Baixar e executar modelos de IA** (ex: Llama, Mistral, Gemma, etc.)
- Usar esses modelos via **terminal**
- Rodar um **servidor local (API HTTP)** para integrar com aplicações (ex: **LangChain**, **Python**, **Unity**, etc.)

---

### Comandos Úteis no Terminal


```bash
ollama serve                    # Rodar aplicação Ollama
ollama --version                # Verificar se o Ollama está instalado
ollama pull llama3.2:latest     # Baixar um modelo (pull)
ollama list                     # Listar modelos instalados
ollama rm llama3.2:latest       # Remover um modelo instalado
ollama run llama3.2:latest      # Rodar um modelo (modo chat)
ollama ps                       # Listar LLMs em execução 
ollama stop nome-do-modelo      # Parar uma LLM em execução 
ollama show llama3.2:latest     # Ver informações de um modelo