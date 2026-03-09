### Split Phase

Este tópico se refere à refatoração **Split Phase**, onde um processo que realiza múltiplas etapas diferentes é dividido em fases separadas.

Muitas vezes uma função acaba misturando responsabilidades como interpretar dados de entrada e executar regras de negócio. Isso pode tornar o código mais difícil de entender, testar e reutilizar.

Ao aplicar **Split Phase**, separamos essas etapas em funções distintas. Normalmente a primeira fase transforma ou interpreta os dados de entrada, enquanto a segunda fase realiza o processamento ou cálculo baseado nesses dados.

Essa separação melhora a organização do código, torna cada etapa mais clara e facilita a manutenção e evolução da lógica.
