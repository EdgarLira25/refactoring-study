### Replace Inline Code with Function Call

Este exemplo demonstra o padrao de refatoracao Replace Inline Code with Function Call.
Esse refactor consiste em substituir um bloco de codigo repetido por uma chamada para funcao dedicada.
Quando a mesma logica aparece em varios pontos, encapsular em funcao reduz duplicacao e melhora legibilidade.

Útil para funções que já existem (ex: startswith de string), quando não, é melhor aplicar extract method.
