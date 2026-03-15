### Replace Parameter With Query

Este topico se refere a refatoracao Replace Parameter With Query, onde removemos parametros que podem ser obtidos internamente a partir do proprio objeto do contexto.
Quando um argumento e derivavel do estado ja disponivel, a assinatura fica verbosa e aumenta risco de inconsistencias.
Ao consultar o valor dentro da funcao, reduzimos duplicacao de conhecimento e simplificamos a chamada.
