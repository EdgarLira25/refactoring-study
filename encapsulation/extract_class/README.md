### Extract Class

Este tópico se refere à refatoração Extract Class, onde uma classe muito grande e com responsabilidades diferentes é dividida em classes menores.
Quando uma classe mistura dados de contato, endereço e cobrança, por exemplo, ela tende a ficar difícil de entender, testar e evoluir.
Ao separar essas responsabilidades em classes específicas, o código fica mais coeso e mudanças futuras se tornam mais seguras.

- Use quando a classe possui grupos de campos e métodos que formam um subdomínio claro (como endereço, pagamento ou contato).
- Use quando alterações em uma parte da classe quebram partes não relacionadas, sinal de baixo encapsulamento.
- O motivo é aumentar coesão, deixando cada classe responsável por um único conjunto de regras.
- O motivo também é reduzir acoplamento e facilitar testes, manutenção e reutilização dos comportamentos extraídos.
