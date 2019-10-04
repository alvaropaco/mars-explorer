# CargoX Coding Challenger 
[![CircleCI](https://circleci.com/gh/alvaropaco/mars-explorer.svg?style=svg)](https://circleci.com/gh/alvaropaco/mars-explorer/tree/master)

### Description

Cargox Coding Challenge 
Bem vindo! Se você está aqui é porque gostamos do seu perfil e 
queremos conhecer um pouco mais sobre suas habilidades como 
desenvolvedor.

### Teste 

Introdução 

Sua aplicação deve rodar sem erros, e você deve prover 
evidências suficientes de que sua solução está correta por, 
pelo menos, funcionar da maneira esperada para os dados de 
teste fornecidos abaixo. 
SONDAS DE MARTE Um esquadrão de sondas robóticas da NASA 
pousará em um platô em Marte. Este platô, que curiosamente tem 
formato retangular, deve ser percorrido pelas sondas a fim de 
fornecer informações a respeito do terreno através das câmeras 
instaladas nas sondas, as quais enviarão as imagens à Terra. 

A posição da sonda e sua localização são representadas por uma 
combinação de coordenadas x e y, além de uma letra 
representando um dos quatro principais pontos cardeais da rosa 
dos ventos (N, S, L, W -- lembre-se que o código deve ser em 
inglês, portanto a representação do Oeste é 'W', não 'O'). 

O platô é dividido em um quadriculado para simplificar a 
navegação. Um exemplo de posição seria 0, 0, N, que significa 
que a sonda está no canto inferior esquerdo apontando para o 
Norte. 

Para controlar a sonda, a NASA envia uma série simples de 
letras. As letras possíveis são 'L', 'R' e 'M'. 'L' e 'R' 
fazem a sonda girar 90 graus para a esquerda ou direita 
respectivamente, sem sair de sua posição atual. 'M' significa 
"mova-se para frente uma posição no quadriculado do platô e 
mantenha a direção para onde você está apontando". 
Considere que o quadrado diretamente ao Norte de (x, y) é (x, 
y+1). 

**ENTRADA: A primeira linha da entrada são as coordenadas do 
canto superior direito do platô -- lembre-se que as 
coordenadas do canto inferior esquerdo são 0,0.**

O resto da entrada são as informações relativas às sondas que 
foram aterrissadas em Marte. Cada sonda tem duas linhas de 
entrada: a primeira linha fornece a posição inicial da sonda; 
a segunda linha contém uma série de instruções sobre como a 
sonda deve explorar o platô. 

A posição é composta por dois números inteiros e uma letra 
separados por espaço, correspondendo às coordenadas x e y e à 
direção para onde a sonda aponta. 

Cada sonda executará seus movimentos em sequência, ou seja, a 
segunda sonda só começará a se mover depois que a primeira 
tiver terminado sua movimentação. 

SAÍDA A saída de cada sonda deverá ser suas coordenadas finais 
e a direção para onde ela aponta. 

> EXEMPLO: Dados de entrada para testes: 5 5 1 2 N LMLMLMLMM 3 3 
E MMRMMRMRRM 

**Saída esperada: 1 3 N 5 1 E** 
Submissão 
Utilize Git para versionamento do seu projeto. Faça um FORK e 
submeta um PULL REQUEST para este repositório com a sua 
solução. 

Atenção: Não criar um repositório público com o conteúdo do 
desafio ou solução. 

#### Critérios de avaliação 
- Compreensão dos requisitos 
- Fornecer documentação explicando como como rodar e testar 
localmente. 
- Engenharia de software 
- Cobertura de testes 
- Versionamento 
- Arquitetura do código 
- Separação de responsabilidades 
- Manutenabilidade 
##### Diferenciais 
- Utilizar Docker e docker-compose. 
- Considerações finais 

Sinta-se livre para entrar em contato conosco sempre que 
necessário! 
A CargoX agradece seu interesse e te deseja BOA SORTE! 

## How To Run

The proggram is executed running the docker image passing the input line by arguments:

`docker run -it cargox python main.py 5 5 1 2 N LMLMLMLMM 3 3 E MMRMMRMRRM`

## How To the tests

Simillar to the execution, just run the following command line:

`docker run -it cargox nose2 --with-coverage`

## Final considerations

As a coding challenge this test required a logicall think to solve the main problem of exploration and orientation and proggramming skills with Objects, collections and iterations. Was a good exercise for me =)