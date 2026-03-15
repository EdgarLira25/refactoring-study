### Remove Setting Method

Este topico se refere a refatoracao Remove Setting Method, onde removemos setters e definimos estado essencial no momento de construcao do objeto.
Quando o estado principal pode ser alterado livremente por setter, a classe pode entrar em combinacoes invalidas ao longo do ciclo de vida.
Ao reduzir mutabilidade e restringir mudancas, aumentamos consistencia e previsibilidade do dominio.

Isso é útil para, por exemplo, IDs que nunca mudam, campos que não devem ser editados e etc.
