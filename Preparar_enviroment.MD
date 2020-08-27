# Preparando Ambiente para rodar o programa (Enviroment)

## Preparativo no Mac:
### INSTAR PYTHON E MINICONDA

EXIBIR ARQ OCULTO: Use o atalho de teclado Command (⌘) + Shift + . (sim, o ponto final) dentro do Finder; 

## Preparativo no Terminal:
> # verificar se tem Python instalado, retorna o path 
> which python3
> # verificar versão do Python
> python3 -v
> # criar diretoria
> mkdir repositorios
> * Atualizar python 3
> https://www.python.org/downloads/
> Baixar arquivo e Instalar

## Baixar miniconda
> https://docs.conda.io/en/latest/miniconda.html
> Baixar e instalar
> bash Miniconda3-latest-MacOSX-x86_64.sh
> export PATH=/User/wpessoa/miniconda3/bin:$PATH

> conda deactivate
> conda create -n py3 python=3
> conda activate py3

## FIM INSTALADO MINICONDA

## INSTALAÇAO JUPYTER

> conda install -c conda-forge jupyterlab
> pip install jupyterlab
> jupyter lab

