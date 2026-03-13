### Split Loop

Este exemplo demonstra o padrao de refatoracao Split Loop.
Esse refactor consiste em dividir um unico loop que executa responsabilidades diferentes em multiplos loops menores e focados.
Quando um loop calcula metricas distintas ao mesmo tempo, a leitura tende a ficar mais confusa e qualquer mudanca pode gerar efeitos colaterais em regras nao relacionadas.
Ao separar os objetivos em loops independentes, o codigo fica mais explicito, mais facil de testar e mais seguro para evoluir.
