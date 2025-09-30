# Projeto de Programação Funcional: Sistema de Análise de Desempenho de Alunos

## 1. Objetivo do Projeto

O objetivo deste projeto é desenvolver um sistema em Python para análise de desempenho de alunos, aplicando exclusivamente conceitos e técnicas do paradigma de programação funcional. O sistema realiza cálculos de médias, determina o status de aprovação e extrai estatísticas de uma lista de alunos, demonstrando o uso de funções puras, imutabilidade, funções de alta ordem, closures, lambdas e list comprehensions.

## 2. Equipe

| Nome Completo   | Matrícula    | Papel no Projeto                  |
| --------------- | ------------ | --------------------------------- |
| José Danilo de Sousa       | 2326306    | Gerente de Projeto e Documentação |
| Carlos Cauan     | 2326258    | Desenvolvedor Principal (Backend) |
| Jonarta Santiago Soares     | 2327349    | Desenvolvedor Secundario (Auxiliar) |


## 3. Requisitos do Projeto

### 3.1. Requisitos Funcionais (RF)

| ID    | Descrição                                                                      |
| ----- | ------------------------------------------------------------------------------ |
| RF01  | O sistema deve ser capaz de calcular a média final de cada aluno a partir de uma lista de notas. |
| RF02  | O sistema deve permitir a definição de uma nota de corte para aprovação.       |
| RF03  | O sistema deve determinar o status de cada aluno como "Aprovado" ou "Reprovado" com base na nota de corte. |
| RF04  | O sistema deve ser capaz de listar os nomes de todos os alunos aprovados.       |
| RF05  | O sistema deve identificar e exibir o aluno com o melhor desempenho (maior média). |

### 3.2. Requisitos Não Funcionais (RNF)

| ID    | Descrição                                                                      |
| ----- | ------------------------------------------------------------------------------ |
| RNF01 | O código deve ser implementado em Python 3.8 ou superior.                      |
| RNF02 | O código deve aderir estritamente aos princípios da programação funcional, evitando efeitos colaterais e mutabilidade de estado. |
| RNF03 | O projeto deve incluir pelo menos uma função lambda, uma list comprehension, uma closure e uma função de alta ordem. |
| RNF04 | O código deve ser modular, limpo e bem comentado para facilitar a compreensão.   |
| RNF05 | O projeto deve incluir um conjunto de testes unitários para garantir a corretude das funções principais. |
| RNF06 | A execução do programa principal deve ser feita através de um terminal (console). |

## 4. Mapeamento de Requisitos para Funções

| Requisito | Função(ões) no Código (`analise_desempenho.py`)                              |
| --------- | -------------------------------------------------------------------------- |
| RF01      | `calcular_media(aluno)`                                                    |
| RF02      | `criar_verificador_status(nota_de_corte)`                                  |
| RF03      | A função interna retornada por `criar_verificador_status`                  |
| RF04      | `obter_nomes_aprovados(alunos_processados)`                                |
| RF05      | `encontrar_melhor_aluno(alunos_processados)`                               |

## 5. Aplicação dos Conceitos de Programação Funcional

Esta seção detalha onde cada conceito obrigatório de programação funcional foi aplicado no código.

### 5.1. Função de Alta Ordem (Higher-Order Function)

* **Conceito:** Uma função de alta ordem é uma função que recebe outra função como argumento ou retorna uma função como resultado.
* **Aplicação:** A função `processar_dados_alunos` é um exemplo claro. Ela recebe a lista de alunos e uma `funcao_processamento` como argumento, aplicando-a a cada elemento da lista. Isso permite reutilizar a lógica de iteração para diferentes operações (como calcular média ou definir status), tornando o código mais genérico e declarativo.

    ```python
    def processar_dados_alunos(
        alunos: List[Dict],
        funcao_processamento: Callable[[Dict], Any]
    ) -> List[Any]:
        # ...
        return [funcao_processamento(aluno) for aluno in alunos]
    ```

### 5.2. Closure

* **Conceito:** Uma closure ocorre quando uma função aninhada (interna) acessa variáveis do escopo da função externa, mesmo após a função externa ter concluído sua execução. A função interna "lembra" do ambiente em que foi criada.
* **Aplicação:** A função `criar_verificador_status(nota_de_corte)` implementa este conceito. Ela retorna a função `verificar`, que continua tendo acesso à variável `nota_de_corte` de seu escopo pai. Isso nos permite criar "fábricas" de funções de verificação com diferentes critérios (e.g., uma para nota de corte 7, outra para nota 5).

    ```python
    def criar_verificador_status(nota_de_corte: float) -> Callable[[float], str]:
        def verificar(media: float) -> str:
            return "Aprovado" if media >= nota_de_corte else "Reprovado"
        return verificar
    ```

### 5.3. List Comprehension

* **Conceito:** Uma forma concisa e legível de criar listas em Python. A sintaxe `[expressao for item in iteravel if condicao]` permite gerar uma nova lista aplicando uma expressão a cada item de uma sequência, opcionalmente filtrando os itens.
* **Aplicação:** A função `obter_nomes_aprovados` utiliza uma list comprehension para criar uma lista contendo apenas os nomes dos alunos cujo status é "Aprovado".

    ```python
    def obter_nomes_aprovados(alunos_processados: List[Dict]) -> List[str]:
        return [aluno['nome'] for aluno in alunos_processados if aluno['status'] == 'Aprovado']
    ```

### 5.4. Função Lambda

* **Conceito:** Uma função anônima, pequena e de uma única expressão. É frequentemente usada como argumento para funções de alta ordem, como `map()`, `filter()`, `sorted()` ou `max()`.
* **Aplicação:** Na função `encontrar_melhor_aluno`, uma função `lambda` é usada como o argumento `key` para a função `max()`. Ela instrui `max` a comparar os dicionários de alunos com base no valor da chave `'media'`, evitando a necessidade de definir uma função nomeada separada para uma tarefa tão simples.

    ```python
    def encontrar_melhor_aluno(alunos_processados: List[Dict]) -> Dict:
        return max(alunos_processados, key=lambda aluno: aluno['media'])
    ```

## 6. Como Executar o Projeto

1.  **Pré-requisitos:**
    * Python 3.8 ou superior instalado.

2.  **Executar a Aplicação Principal:**
    Abra um terminal na pasta do projeto e execute o seguinte comando:
    ```bash
    python analise_desempenho.py
    ```
    Isso executará a função `main()` e exibirá o relatório de análise no console.

3.  **Executar os Testes:**
    Para garantir que todas as funções estão operando corretamente, execute os testes unitários:
    ```bash
    python test_analise_desempenho.py
    ```

## 7. Avisos

Este projeto utilizou Read.me para formatar e Google/Ava para fonte de pesquisa. O projeto foi simples porem deu chance de aprender mais para uma parcela da equipe.