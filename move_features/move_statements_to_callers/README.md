### Move Statements to Callers

Este exemplo demonstra o padrao de refatoracao Move Statements to Callers.
Esse refactor consiste em mover comandos para os pontos de chamada quando eles nao devem ficar dentro de uma funcao generica.
Quando uma funcao comeca a assumir regras especificas de todos os cenarios, ela fica inchada e perde reutilizacao.
