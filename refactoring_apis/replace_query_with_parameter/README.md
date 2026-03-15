### Replace Query With Parameter

Este topico se refere a refatoracao Replace Query With Parameter, onde removemos consultas internas e passamos o valor necessario como argumento explicito.
Quando uma funcao consulta dependencias globais ou servicos internos, ela fica mais acoplada e dificil de testar isoladamente.
Ao receber o valor por parametro, a funcao ganha previsibilidade e o chamador controla melhor o contexto.
