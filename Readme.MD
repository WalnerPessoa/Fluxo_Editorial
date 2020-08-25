## Projeto automação de processo do NGE
___
Tranformação Digital:
===
### Resumo das tecnicas aplicadas:
Será realizada uma trasnformação digital no processo do NGE por meio de técnicas de scraping de arquivo Word, uso de algoritmos de Random Forest e Regressão logistica para uso de Machine Learning.
### Descrição do Problema:
NGE é o **Núcleo de Gestão Editorial** da Gerência de Publicidade da Confederação Nacional da Indústria, sediada em Brasília/DF.
Numa das primeira fases do processo, o NGE recebe um arquivo Word (enviado pela área demandante) e envia para o fornecedor estimar a quantidade de páginas diagramadas e o valor desse serviço. Ele analisa a número de caracters, quantidade de figuras/fotos/ilustrações/infográficos e faz uma estimativa da quantidade final que o livro terá. Ou seja, pode chegar um arquivo word com 40 páginas e a estimativa da diagrmação poderá ser 80 páginas. Nessa etapa é gerada uma planilha excel que descreve os custos para esse serviço de acordo com o numero de páginas diagramadas. O NGE envia esse documento para a área demandante com o valor de quanto será o a execução desse job. As regras de preço e desconto da planilha excel são feitas pelo fornecedor á luz de um contrato de Licitação em vigor na casa. 

O **problema acontece porque a estimativa feita pelo fornecedor não é precisa**, pois na fase de gerar a Nota fiscal o valor (que tem como base a quantidade de páginas) fica muito inferior ao estimado. Essa situação gera um desconforto grando junto à área demandante porque os valores não batem. O valor da planilha estimada fica muito diferente do valor da Nota Fiscal. Seguindo o exemplo citado no parágrafo anterior, é passado valor de 80 páginas para a área técnica numa primeira fase e um valor de 60 paginas na fase da NF.  
### Métodos computacionais
1. scraping python 
Criar um codigo para raspar as informações do arquivo Word como quantidade de caracteres, quantidade de imagens, quantidade de tabela. 
e o fornecedor avalia a partir de quantidade de fotos, tabelas e quantidade de caracteres a quantidade de páginas que o documento terá após aplicação do projeto gráfico. Ou seja, quantas páginas terá o livro depois de diagramado.
1. uso do pythom para ler arquivos word e gerar tabela
2. uso de modelos de regreção logistica para determinar o que altera a quantidade de páginas no final do processo editorial. Tarefa necessária para estimar os jobs no inicio do processo.

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
 