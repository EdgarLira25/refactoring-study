### Introduce Special Case

Este topico se refere a refatoracao Introduce Special Case, onde um caso especial (como `None`, vazio ou ausente) passa a ser representado por um objeto dedicado com o mesmo contrato do caso normal.
Quando o codigo espalha verificacoes repetidas como `if x is None`, a regra de negocio fica poluida e o fluxo principal perde clareza.
Ao introduzir um objeto especial, removemos condicionais duplicadas, centralizamos o comportamento padrao e deixamos a API mais uniforme.

Quando usar:
- Quando varios metodos repetem o mesmo `if/else` para tratar ausencia de dados.
- Quando o comportamento padrao para um caso especial e estavel e conhecido.
- Quando voce quer reduzir branching e simplificar leitura do fluxo principal.
- Quando um objeto nulo explicito (Null Object) torna o dominio mais legivel.

Quando evitar:
- Quando o caso especial exige tratamento muito diferente e nao compartilha o mesmo contrato.
- Quando esconder o caso especial pode mascarar erro de dados que deveria falhar explicitamente.
