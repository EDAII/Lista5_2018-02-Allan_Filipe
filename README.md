## Lista 5 - Algoritmos Ambiciosos
### Sistema de Moedas para Troco e Definidor de Maior Quantidade de Tarefas em 24h

##### Alunos

| Matrícula | Nome | GitHub |
|--|--|--|
| 15/0029624 | Allan Jefrey Pereira Nobre | @AllanNobre |
| 15/0059213 | Filipe Coelho Hilário Barcelos | @FilipeKN4 |

##### Para executar
O ambiente deve ser configurado para a utilização do framework Django na versão 2.1. Após a configuração, deve-se executar o comando abaixo: 

```sh
$ python3 manage.py runserver
```

Após a execução abra o link do servidor em http://127.0.0.1:8000/.

##### Descrição

Escolhe-se qual algoritmo deseja-se e executar entre Greed - Coin Changing e Greed - Interval Scheduling.
Lê-se um arquivo ".csv" de valores, nos quais são executados nos dois algoritmos. No Greed - Coin Changing é executado o algoritmo que define qual o menor número de moedas brasileiras necessárias para entregar o valor dos trocos desejados. No Greed - Interval Scheduling é executado o algoritmo que define quais são as atividades que podem ser realizadas para que a quantidade máxima delas seja alcançado no período de 24 horas.

##### Visualização

Para a visualização dos resultados foi utilizado o Framework Django da linguagem de programação Python, de modo que foi possível criar uma interface Web estilizada por meio do framework Bootstrap.  

##### Greed - Coin Changing

São indicados na tela os valores do troco com as menores quantidades de moedas brasileiras possíveis necessárias para entregá-los, bem como o tempo de execução do algoritmo inteiro e para cada um dos trocos.

##### Greed - Interval Scheduling

São indicados na tela todas as atividades com seus horários de término e início e se ela foi selecionada como uma atividade a ser feita ou não, bem como o tempo de execução do algoritmo inteiro, quantidade total de atividades e a quantidade máxima possível de atividades a serem feitas com os horários dados.

##### Observações

Seguem dois ".csv" de exemplo de entrada para a aplicação, um para o Greed - Coin Changing e outro para o Greed - Interval Scheduling.