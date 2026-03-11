### Encapsulate Collection

Este tópico se refere à refatoração **Encapsulate Collection**, onde uma coleção deixa de ser manipulada diretamente por código cliente e passa a ser controlada por uma classe.
Quando várias partes do sistema acessam e alteram a mesma lista diretamente, regras de inclusão, remoção e substituição acabam espalhadas e mais difíceis de manter.
Ao encapsular a coleção, essas regras ficam centralizadas em um único ponto, reduzindo acoplamento e tornando mudanças futuras mais seguras.
