# Tabela 1 - PLANO DE ATIVIDADES DE ESTÁGIO CURRICULAR
###
### Elenco de atividades a desenvolver no período de 17/08 a 18/12 dentro da carga horária de 165 horas. 

Projeto automação de processo do NGE (165 horas)
Descrição do problema: A área financeira da diretoria de gerencia de propaganda e publicidade recebe uma estimativa dos fornecedores de quantidade de páginas e valor do serviço. Essa estimativa é formulada a partir do arquivo Word que o demandante envia para NGE. O problema encontra-se na discrepância entre o valor que o gerente que assina no início do proceso e o valor no final do processo, na geração da nota fiscal. Esses dados tem valores muito distintos, chegando a um indice de 50% de diferença. Um erro muito alto.
O objetivo desse projeto é achar uma solução tecnológica por meio de machine learning para fazer uma estimativa com menor variação de erro. 

- 1.1 Desenvolver método Get_file_word (45 horas)
Scraping python Criar um método em python para raspar (scraping) as informações do arquivo Word obtendo informações como quantidade de caracteres, quantidade de imagens, quantidade de tabela. Esse método irá alimentar o vetor input do método Make_table.

- 1.2 Desenvolver método Make_Table (45 horas)
Existe uma planilha excel feita pela área financeira da Gerência de Publicidade e Propaganda que contém os dados da área de compras dessa gerência que contém o histórico das quantidade de páginas final de cada processo de editoração. O método Make_table irá manipulação de vetores (vetor input) por meio da biblioteca Pandas, Numpy e outras. Criar esse método em python para montar um vetor em python que será o vetor  input para o treinamento do modelo de Machine learning. . Esse código irá completar essa tabela para uso do metodo de aprendizagem de máquina.

- 1.3 Método inferir_resultados (75 horas)
Treinamento com algorítmos Random Forest e Regressão Logistica (Machine Learning). Criar e testar um método para treinar um modelos de Random Forest ou Regreção Logistica para encontrar a melhor acurácia na previsão dos valores estimados de páginas diagramadas, ou seja inferir a quantidade de páginas diagramadas para o processo editorial com maior probabilidade de acerto.
