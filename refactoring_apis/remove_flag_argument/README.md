### Remove Flag Argument

Este topico se refere a refatoracao Remove Flag Argument, onde removemos booleanos de controle e substituimos por metodos explicitos para cada comportamento.
Quando um metodo recebe uma flag para decidir fluxo, ele passa a ter responsabilidades misturadas e intencao menos clara.
Ao separar os caminhos em chamadas distintas, a API fica mais legivel e evita combinacoes de uso ambiguas.
