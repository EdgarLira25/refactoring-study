### Remove Dead Code

Este exemplo demonstra o padrao de refatoracao Remove Dead Code.
Remove Dead Code consiste em eliminar trechos de codigo que nao sao mais executados, nao sao mais referenciados ou representam caminhos obsoletos no sistema.
Mesmo quando esse codigo aparentemente nao causa erros diretos, ele aumenta o custo de manutencao, dificulta leitura e pode induzir quem mantem o sistema a conclusoes incorretas sobre o comportamento real da aplicacao.

Codigo morto costuma aparecer em formas como:
- funcoes antigas que nao possuem mais chamadas
- condicionais com ramos impossiveis de acontecer
- variaveis, flags e parametros sem uso
- comentarios de "fallback" que nao refletem mais o fluxo atual

Remover codigo morto e valioso porque:
- reduz ruido cognitivo para quem le e altera o codigo
- diminui superficie para bugs em futuras mudancas
- facilita testes, revisao e onboarding
- melhora sinalizacao da regra de negocio realmente vigente

Boas praticas ao aplicar esse refactor:
- confirme com testes e busca de referencias que o trecho nao e usado
- remova de forma pequena e incremental
- prefira apagar por completo em vez de manter blocos comentados
- registre no historico de commit o contexto da remocao

Resumo: Remove Dead Code e uma refatoracao de higiene estrutural. Ela nao muda a regra de negocio esperada, mas melhora significativamente clareza, confiabilidade e velocidade de evolucao do codigo.
