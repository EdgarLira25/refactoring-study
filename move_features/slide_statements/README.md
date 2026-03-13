### Slide Statements

Este exemplo demonstra o padrao de refatoracao Slide Statements.
Esse refactor consiste em reorganizar a ordem de comandos para agrupar blocos relacionados.
Quando variaveis sao declaradas longe de onde sao usadas, ou quando calculos e validacoes ficam intercalados sem criterio, o fluxo fica mais dificil de entender e manter.
Ao aproximar instrucoes que pertencem ao mesmo objetivo, a leitura fica mais linear e a intencao do codigo se torna mais explicita, sem alterar o comportamento final.
Nao há casos de exemplo detalhados neste topico por conta da simplicidade do padrao.
