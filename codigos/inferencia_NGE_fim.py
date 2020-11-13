import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#Importando o modelo machine learnig
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--fileInput", required=True, help="path + file to start process")
args = vars(ap.parse_args())

# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["fileInput"]))

# importar csv da base de jobs sem nota fiscal ou seja sem o valor final de páginas confirmado

data_semNF = pd.read_csv("nge_dados_input_semNF.csv")

#
# normalizar a quantidade de caracteres
#
data_semNF.loc[:,'qtd_carc_normal'] = pd.Series((data_semNF.qtd_carc-data_semNF.qtd_carc.min())/(data_semNF.qtd_carc.max()-data_semNF.qtd_carc.min()))

