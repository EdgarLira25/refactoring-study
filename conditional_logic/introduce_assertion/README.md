### Introduce Assertion

Este topico se refere a refatoracao Introduce Assertion, onde adicionamos `assert` para explicitar suposicoes que o codigo faz sobre estado, entrada ou fluxo.
O objetivo nao e tratar erro de usuario final, e sim falhar rapido quando uma premissa interna do sistema for violada.
Isso ajuda a detectar bugs cedo, documentar invariantes do dominio e evitar que o sistema continue com dados inconsistentes.

Quando usar:
- Quando existe uma pre-condicao que sempre deveria ser verdadeira antes de executar uma regra.
- Quando um valor derivado depende de um estado interno valido e qualquer desvio indica bug.
- Quando voce quer documentar invariantes de dominio de forma executavel e verificavel.
- Quando uma condicao "impossivel" aparece em codigo legado e voce quer tornar essa expectativa explicita.
- Quando uma violacao precisa ser descoberta em desenvolvimento e testes, antes de virar comportamento silencioso em producao.

Quando evitar:
- Nao use `assert` para validar entrada externa de usuario, API ou banco; nesses casos use validacoes e erros de dominio apropriados.
- Nao use `assert` como substituto de tratamento de erro de negocio recuperavel.
- Nao use `assert` com efeitos colaterais; a expressao deve apenas verificar estado.
