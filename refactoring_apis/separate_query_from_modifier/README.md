### Separate Query From Modifier

Este topico se refere a refatoracao Separate Query From Modifier, onde uma operacao que consulta dados e separada de outra que altera estado.
Quando um metodo retorna informacao e ao mesmo tempo modifica atributos internos, o contrato fica ambiguo e dificulta testes previsiveis.
Ao separar consulta de modificacao, o comportamento fica mais explicito e os efeitos colaterais ficam controlados.
