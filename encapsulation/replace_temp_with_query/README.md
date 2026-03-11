### Replace Temp with Query

Este tópico se refere à refatoração Replace Temp with Query, onde variáveis temporárias que armazenam resultados intermediários passam a ser substituídas por consultas em métodos.
Quando muitos valores temporários são usados dentro da mesma rotina, o fluxo pode ficar mais difícil de entender e de evoluir.
Ao extrair esses cálculos para métodos de consulta, o código tende a ficar mais legível, com responsabilidades mais claras e menor risco de inconsistência entre cálculos relacionados.
