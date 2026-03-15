### Preserve Whole Object

Este topico se refere a refatoracao Preserve Whole Object, onde passamos o objeto completo em vez de enviar varios campos isolados para uma funcao.
Quando muitos atributos de um mesmo objeto sao passados separadamente, a assinatura cresce e cria acoplamento com detalhes internos.
Ao preservar o objeto inteiro, reduzimos ruido de parametros e mantemos a semantica de dominio mais clara.
