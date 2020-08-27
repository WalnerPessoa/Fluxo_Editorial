## Projeto automação de processo do NGE
___
Tranformação Digital:
===
### Resumo das técnicas aplicadas:
Será realizada uma trasnformação digital no processo do NGE por meio de técnicas de scraping de arquivo Word, uso de algoritmos de Random Forest e Regressão Logistica para treinamento supervisionado de Machine Learning. 
### Quem é o demandante:
NGE é o **Núcleo de Gestão Editorial** da Gerência de Publicidade e Propaganda da Confederação Nacional da Indústria, sediada em Brasília/DF. Esse Núcleo é responsável pela produção de livros das entidades CNI, SESI, SENAI e IEL (Departamento Nacionais SESI/SENAI/IEL apenas). 
### Descrição do Problema:
Numa das primeira fases do processo editorial, o NGE recebe um arquivo Word (enviado pela área demandante) e envia para o fornecedor licitado estimar a quantidade de páginas diagramadas e o valor desse serviço. O fornecedor analisa o número de caracteres, quantidade de figuras/fotos/ilustrações/infográficos e com base nessa analise e no comportamento da publicação que deseja alcançar, faz uma estimativa da quantidade final de páginas que o livro terá após ser diagramado. Por exemplo, pode chegar um arquivo word com 40 páginas e a estimativa da diagramação ser de 80 páginas. Nessa etapa é gerada uma planilha excel que descreve os custos para esse serviço de acordo com o número de páginas diagramadas. A precificação é realizada por meio da quantidade de páginas versus o valor unitário de cada página determinado no contrato de Licitação em vigor na casa. Feito essa precificação, o fornecedor encaminha a planilha de custos (Excel) para o NGE avaliar e caso esteja em consonância com o que preconiza o contato, a planilha é enviada para a área demandante aprovar e assim iniciar a execução desse job.

Nesse processo, **o problema acontece no momento em que o NGE apresenta a planilha de custos (Excel) para a área demandante**, pois como cada publicação tem um comportamento diferente, a estimativa feita pelo fornecedor nem sempre é precisa, muitas vezes resulta em mais de 100% de acréscimo de páginas em relação ao arquivo Word recebido, impactando diretamente no valor apresentado para aprovação e gera um certo desconforto para a área demandante. 

Cabe ressaltar ainda que ao final da diagramação e entrega da publicação, conforme preconiza o contrato, o fornecedor realiza o faturamento somente da quantidade de páginas que a publicação final alcançou. Seguindo o exemplo citado anteriormente, ficaria da seguinte forma: o arquivo word tem 40 páginas, a planilha estimada consta o valor referente a 80 páginas e a nota fiscal é gerada com o valor de 60 paginas. Esse faturamento sempre será menor do que foi aprovado, pois só é possível pagar o que de fato foi entregue. Sendo assim, na maioria dos casos o valor fica muito diferente ao valor estimado e aprovado formalmente. Apesar de ser sempre a menor. 

Enfim, a estimativa alta, acontece porque toda a avaliação (por parte do fornecedor) de quantidade de páginas diagramadas é feita sem uma metodologia precisa e esse problema do valor da planilha estimada ficar muito diferente do arquivo Word recebido já foi mapeado há meses e é **o foco desse trabalho de Transformação Digital.** 
### Métodos computacionais
1. **Scraping python** 
Criar um método (classe) em python para raspar (scraping) as informações do arquivo Word obtendo informações como quantidade de caracteres, quantidade de imagens, quantidade de tabela. Esse método irá alimentar o vetor input do treinamento de Machine Learning.
2. **Manipulação de vetores (vetor input)**
Criar um método (classe) para montar um vetor em python para contruir o vetor (array) input para o treinamento do modelo. Inicialmente já existe uma tabela excel feita pela área financeira da Gerência de Publicidade e Propaganda . Esse código irá completar essa tabela para uso do metodo de aprendizagem de máquina.
3. **Treinamento com algorítmos Random Forest e Regressão Logistica (Machine Learning)**
Criar um  método (classe) para treinar um modelos de Random Forest ou Regreção Logistica para encontrar a melhor acurácia na previsão dos valores estimados de páginas diagramadas, ou seja inferir a quantidade de páginas diagramadas para o processo editorial com maior probabilidade de acerto.

## Veja a lista dos algoritmos mais populares:
https://www.datageeks.com.br/algoritmos-de-machine-learning/

- Regressão Linear
- Regressão logística
- Árvores de Decisão
- Classificação Naive Bayes
- Extreme Gradient Boosting – XGBoost
- SVM (Support Vector Machine)
- Ensemble Methods
- Algoritmos de Agrupamento (Clustering)
- Decomposição em valores singulares
- Análise de Componentes Principais
- Análise de componentes independentes
- KNN (K-vizinhos mais próximos)
- Floresta aleatória ou Random Forest
- Algoritmos de redução dimensional
 