### Pull Up Constructor Body

Este topico se refere a refatoracao Pull Up Constructor Body, onde trechos comuns de construtores de subclasses sao movidos para a superclasse.
Quando inicializacoes iguais se repetem, a evolucao do estado inicial fica espalhada e propensa a inconsistencias.
Ao concentrar o corpo comum no construtor da classe mae, simplificamos as filhas e mantemos o setup uniforme.
