### Encapsulate Field

Este exemplo demonstra o padrão de refatoração **Encapsulate Field**.

Esse refactor consiste em restringir o acesso direto a um atributo de uma classe, passando a controlá-lo por meio de métodos ou propriedades.
O objetivo é proteger o estado interno do objeto e garantir que qualquer modificação passe por um ponto controlado.

Encapsular um campo permite:

* evitar alterações indevidas no estado do objeto
* aplicar validações antes de modificar valores
* centralizar regras relacionadas ao atributo
