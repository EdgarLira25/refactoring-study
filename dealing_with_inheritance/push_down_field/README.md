### Push Down Field

Este topico se refere a refatoracao Push Down Field, onde um campo da superclasse e movido para a subclasse que precisa dele.
Quando um atributo existe na classe mae mas so faz sentido para parte da hierarquia, o modelo fica confuso.
Ao empurrar o campo para baixo, evitamos estado inutil nas classes que nao usam essa informacao.
