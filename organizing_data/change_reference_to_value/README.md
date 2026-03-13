### Change Reference to Value

Este tópico se refere à refatoração Change Reference to Value, onde um objeto referenciado é transformado em objeto de valor.
Quando identidade compartilhada não é necessária, usar referência pode introduzir efeitos colaterais inesperados por mutação em múltiplos pontos.
Ao tratar o dado como valor, comparações passam a focar conteúdo e o comportamento tende a ficar mais previsível, com menor risco de alteração acidental global.
