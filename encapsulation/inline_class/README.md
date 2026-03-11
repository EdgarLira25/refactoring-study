### Inline Class

Este tópico se refere à refatoração Inline Class, onde uma classe pequena e com pouca responsabilidade é incorporada de volta na classe cliente.
Quando uma classe foi extraída, mas acabou sem comportamento relevante próprio, ela pode adicionar complexidade sem trazer ganho real de design.
Ao fazer inline dessa classe, o modelo fica mais simples, com menos indireções e leitura mais direta do fluxo de negócio.

- Use quando a classe extraída quase não tem comportamento próprio e só repassa dados.
- Use quando a existência da classe intermediária aumenta complexidade sem melhorar encapsulamento.
- O motivo é simplificar o modelo, removendo camadas e reduzindo indireções desnecessárias.
- O motivo também é facilitar manutenção e entendimento, mantendo a lógica onde ela realmente pertence.
