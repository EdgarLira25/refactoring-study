### Move Function

Este exemplo demonstra o padrao de refatoracao Move Function.
Esse refactor consiste em mover uma funcao para a classe onde ela representa melhor a regra de negocio.
Quando uma funcao depende mais dos dados de outro objeto do que do proprio objeto onde ela esta hoje, isso geralmente indica localizacao inadequada.
Ao mover a funcao para o lugar certo, o codigo tende a ficar mais coeso, com menor acoplamento acidental e com responsabilidades mais claras no dominio.
Nao há casos de exemplo detalhados neste topico por conta da simplicidade do padrao.
