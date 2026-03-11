### Hide Delegate

Este tópico se refere à refatoração Hide Delegate, onde o objeto cliente deixa de navegar por uma cadeia de objetos para acessar informações internas de outro objeto.
Quando o código chama sequências como `order.customer.address.country`, ele fica mais acoplado à estrutura interna do domínio e se torna mais frágil a mudanças.
Ao esconder a delegação atrás de métodos mais diretos, o código cliente fica mais simples, com menor acoplamento e maior encapsulamento.
