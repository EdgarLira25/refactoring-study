### Replace Derived Variable with Query

Este tópico se refere à refatoração Replace Derived Variable with Query, onde variáveis derivadas passam a ser calculadas por funções de consulta em vez de armazenadas e atualizadas manualmente.
Quando um valor derivado é mantido em variável própria, é comum surgirem inconsistências por esquecimento de atualização após mudanças no estado base.
Ao substituir esse valor por uma query, o resultado passa a ser sempre recalculado a partir da fonte real, aumentando confiabilidade e reduzindo bugs de sincronização.
