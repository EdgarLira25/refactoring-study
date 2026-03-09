### Parameter Object

Este tópico se refere à refatoração **Introduce Parameter Object**, onde vários parâmetros relacionados são agrupados em um único objeto.
Quando uma função recebe muitos parâmetros que representam um mesmo conceito, isso pode indicar um *code smell* conhecido como **Long Parameter List**.
Criar um objeto que represente esse conjunto de dados melhora a organização do código, facilita a leitura e permite que comportamentos relacionados a esses dados sejam encapsulados.
