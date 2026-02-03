# Tools

Ferramentas (tools) são funções Python, scripts ou serviços externos que expomos
para que a IA execute em nosso nome. Cada tool descreve quais argumentos aceita
e o que devolve, permitindo que o modelo peça ações determinísticas, como
calcular algo, consultar uma API, ler um arquivo e várias outras coisas. Por
isso, a documentação da sua ferramenta é extremamente importante.

### Exemplo

Suponha que você tem uma ferramenta chamada `multiply` que recebe `a` e `b`. Sua
ferramenta está bem documentada, de forma que a IA não terá dificuldades em
saber quando chamá-la:

```python
@tool
def multiply(a: float, b: float) -> float:
    """Multiply a * b and returns the result

    Args:
        a: float multiplicand
        b: float multiplier

    Returns:
        the resulting float of the equation a * b
    """
    return a * b
```

## Por que usar ferramentas com LLMs?

LLMs trabalham apenas com o que está na janela de contexto e no treinamento.

Ferramentas nos permitem ultrapassar essas barreiras:

- Executar cálculos ou transformações determinísticas sem depender da
  "imaginação" do modelo.
- Buscar informações atualizadas em APIs, bancos de dados ou arquivos locais.
- Aplicar regras de negócio específicas do produto sem expô-las ao modelo.
- Integrar a conversa com outros sistemas (e-mails, automações, tickets, etc)
  mantendo rastreabilidade do que foi feito.
