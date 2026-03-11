### Remove Middle Man

Este tópico se refere à refatoração Remove Middle Man, onde uma classe intermediária deixa de apenas repassar chamadas para outro objeto.
Quando muitos métodos de uma classe só delegam para campos internos, essa camada intermediária pode aumentar complexidade sem agregar comportamento real.
Ao remover esse middle man, o cliente acessa o objeto relevante de forma mais direta, reduzindo indireção e deixando o fluxo mais claro.
