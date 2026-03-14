### Replace Conditional with Polymorphism

Este topico se refere a refatoracao Replace Conditional with Polymorphism, onde uma cadeia de condicionais por tipo e substituida por classes com comportamento especifico.
Quando o codigo depende de `if/elif` para decidir regra por categoria, cada novo tipo aumenta acoplamento e risco de regressao.
Ao mover o comportamento para polimorfismo, cada variacao fica isolada, extensivel e mais facil de evoluir sem alterar um bloco central.
