### Replace Loop with Pipeline

Este exemplo demonstra o padrao de refatoracao Replace Loop with Pipeline.
Esse refactor consiste em substituir loops imperativos por uma sequencia declarativa de transformacoes, como filter, map e reduce/sum.
Quando o objetivo principal do codigo e transformar e agregar colecoes, pipelines podem deixar a intencao mais clara e reduzir codigo acidental de controle.
A ideia nao e usar pipeline em qualquer caso, mas sim quando ele melhora legibilidade sem esconder regras de negocio importantes.
