# Refactoring

Repositório para estudos do livro Refactoring de Martin Fowler

---

Refactoring é o processo de melhorar a estrutura interna do código sem alterar seu comportamento externo.
O foco é aumentar legibilidade, reduzir duplicação, melhorar coesão, diminuir acoplamento e tornar mudanças futuras mais seguras.

Boas práticas comuns durante refactoring:
- Fazer mudanças pequenas e incrementais
- Garantir cobertura com testes automatizados
- Manter o sistema funcionando a cada passo
- Nomear melhor variáveis, funções e classes
- Encapsular regras de negócio e dados

Neste repositório, cada pasta apresenta exemplos de "before" e "after" para estudar técnicas de refactoring.

## Resumo sobre Refactoring

Aqui guardei como espaço mais ludico para consulta simples do refactoring e listagem dos padrões.

OBS: A partir do capítulo 6, cada pasta representa um capítulo e seus respectivos padrões

#### Capitulo 1 - Refactoring A First Example

Neste primeiro capítulo, Martin Fowler da um exemplo prático de
refactoring aplicando várias técnicas que ele irá apresentar ao longo do livro

O ponto interessante, está em como ele pensa e aplica todo o refactoring.
- Testa constantemente o código
- Baby steps entre cada passo
- Olhar crítico para cada método, classe, função, loop
- Olhar crítico para os algoritmos, por mais simples que sejam.

Assim, no fim deste capitulo, temos a nossa primeira 'ideia', de como refatorar um código.

É provável que já tenhamos aplicado algum padrão, mesmo sem saber que ele foi formalmente definido no livro de refactoring

#### Capitulo 2 - Principles In Refactoring

Neste capítulo, Martin Fowler repassa sua mentalidade de quando refatorar um código.

Separarei em tópicos, pois é mais simples de compreender

- Refatorar sempre que irá escrever uma feature e tocar em código já existente.
- Usar regra de 3, se for a terceira vez tocando naquele código, refatore, mesmo que apenas um pequeno pedaço
- Refatoração requer testes, se não é 'rewrite', às vezes, não há como escapar, mas enfim.
- Metáfora dos dois Chapéus:
    Chapéu de implementador de feature
    Chapéu de refatorador de código

    -- Nesta metafóra, ele diz que sempre que vamos implementar algo,
        é bom trocar entre os dois chapéus,
        pois código precisa melhorar, para assim,
        melhorar a capacidade do time e mantenabilidade daquele projeto

- Nem sempre refactoring visa performance, por mais que ela seja importante, às vezes 10ms a mais, não é nada, para legibilidade que o código ganhará
- Ele enforça algumas coisas como code ownership, se o código não é 'seu', a refatoração pode ser invasiva
- Reforça a necessidade de haver testes, SEMPRE
- Reforça que CI, ajuda muito a integrar código
- Cita IDE's como um grande auxiliador para refactoring

#### Capitulo 3 - Bad Smelss in Code

Aqui ele faz um catálogo de coisas que fazem o código 'cheirar-mal', irei deixar apenas o index, pois acredito que os nomes são em 80% auto-explicativos

- Mysterious Names
- Duplicated Code
- Long Function
- Long Parameter List
- Global Data
- Mutable Data
- Divergent Change -> Mudanças em módulos que não deveriam ter nada haver com o problema
- Shorgun Surgery
- Feature Envy
- Data Clumps
- Primitive Obsession -> telefone ser string quando há mais valor que apenas os numeros (Ex: DDD)
- Repeated Switches
- Loops
- Lazy Element
- Speculative Generality
- Temporary Fields
- Message Chains
- Middle Man
- Insider Trading
- Large Class
- ALternative Classes With Different Interfaces
- Data Class -> Data class com comportamento**
- Refused Request
- Comments

#### Capitulo 4 - Building tests

Eu poderia resumir, mas resumidamente, escreva testes, eles são importantes,
testes simples, rápidos e com escopo bem definido, sem side effects, ÊNFASE em unitários

#### Capitulo 5 Introducint Catalog:

A partir daqui é um grande catálogo das anotações de Martin Fowler, feito também com a ajuda de seus amigos para definir e questionar cada tipo de refactoring.

#### Capitulo 6 - A First Set Of Refactorings

Segundo o livro, a lista dos principais refactorings para se aprender

- Change Function Declaration
- Combine Function Into Transform
- Combine Functions Into Class
- Encapsulate Field
- Extract Method
- Extract Variable
- Inline Method
- Inline Variable
- Parameter Object
- Rename Variable
- Split Phase
  
#### Capitulo 7 - Encapsulation

Refactorings referentes ao encapsulamento de variáveis, classes e data class

- Encapsulate Collection
- Encapsulate Record
- Extract Class
- Hide Delegate
- Inline Class
- Remove Middle Man
- Replace Primitive With Object
- Replace Temp With Query
- Substitute Algorithm

#### Capitulo 8 - Moving Features

Refactorings referentes a criação, remoção e renomeação de elementos, e por elementos, leia-se, funções, parâmetros, loops e outras estruturas comuns

- Move Field
- Move Function
- Move Statements Into Function
- Move Statements To Callers
- Remove Dead Code
- Replace Inline Code With Function Call
- Replace Loop With Pipeline
- Slide Statements
- Split Loop

#### Capitulo 9 - Organizing Data

Refactorings referentes a principalmente como devemos olhar para 'records' de qualquer natureza, mostrando desde como encapsular estado, como garantir mutabilidade ou imutabilidade quando necessário.
- Change Reference To Value
- Change Value To Reference
- Rename Field
- Replace Derived Variable With Query
- Split Variable

#### Capitulo 10 - Conditional Logic

Refactoring referentes as estruturas de condicionais, if, else, while.
- Consolidate Conditional Expression
- Decompose Conditional
- Introduce Assertion
- Introduce Special Case
- Replace Conditional With Polymorphism
- Replace Nested Conditional With Guard Clauses

#### Capitulo 11 - Refactoring APIs

Refactors referentes a como as chamadas em funções são feitas, parâmetros que não fazem sentido, setter que não deveriam existir, APIs que recebem campos demais e etc.

- Parameterize Function
- Preserve Whole Object
- Remove Flag Argument
- Remove Setting Method
- Replace Command With Function
- Replace Constructor With Factory Function
- Replace Function With Command
- Replace Parameter With Query
- Replace Query With Parameter
- Separate Query From Modifier

#### Capitulo 12 - Dealing With Inheritance

Refactors referentes a herança. Todos são curiosamente, bem intuitivos e o pensamento de OO, inevitavelmente levaria a eles, segue nome dos padrões

- Collapse Hierarchy
- Extract Superclass
- Pull Up Constructor Body
- Pull Up Field
- Pull Up Method
- Push Down Field
- Push Down Method
- Remove Subclasses
- Replace Subclass With Delegate
- Replace Superclass Wih Delegate
- Replace Type Code With Subclasses
