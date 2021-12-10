import pandas as pd
from pathlib import Path
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from controllers.atualizarBD import updateBD

def updateEquipe(n_equipe, n_pontos, n_partidas, n_vitorias, n_empates, n_derrotas, n_gp, n_gc, n_ca, n_cv):
    p = Path(os.getcwd())
    
    df = pd.read_csv(str(p)+"\\database\\dados.csv", encoding="UTF-8", sep=";")
    id = list([df.loc[0:20]["ID"]])
    nome = list([df.loc[0:20]["nome"]])
    pontos = list([df.loc[0:20]["pontos"]])
    vitorias = list([df.loc[0:20]["vitorias"]])
    empates = list([df.loc[0:20]["empates"]])
    derrotas = list([df.loc[0:20]["derrotas"]])
    partidas = list([df.loc[0:20]["partidas"]])
    posicao = list([df.loc[0:20]["posicao"]])
    golsPro = list([df.loc[0:20]["golsPro"]])
    golsContra = list([df.loc[0:20]["golsContra"]])
    saldo = list([df.loc[0:20]["saldo"]])
    cartoesA = list([df.loc[0:20]["cartoesA"]])
    cartoesV = list([df.loc[0:20]["cartoesV"]])

    objeto = {}
    
    i = 0
    for a in list(range(0,20)):
        objeto[a] = [id[0][i], nome[0][i], pontos[0][i], vitorias[0][i], empates[0][i], derrotas[0][i], partidas[0][i], posicao[0][i], golsPro[0][i], golsContra[0][i], saldo[0][i], cartoesA[0][i], cartoesV[0][i]]
        i+=1

    for b in objeto:
        if objeto[b][1] == n_equipe:
            objeto[b][2] = n_pontos
            objeto[b][6] = n_partidas
            objeto[b][3] = n_vitorias
            objeto[b][4] = n_empates
            objeto[b][5] = n_derrotas
            objeto[b][7] = objeto[b][7]
            objeto[b][8] = n_gp
            objeto[b][9] = n_gc
            objeto[b][10] = n_gp - n_gc #saldo
            objeto[b][11] = n_ca
            objeto[b][12] = n_cv

    cont = list(range(0,20))
    dados = sorted(objeto.values(), key=lambda v:v[2], reverse=True)
    dados = dict(zip(cont, dados))
   
    for c in dados:
        dados[c][7] = (c+1)

    df = pd.DataFrame(data=dados.values(), columns=["ID", "nome", "pontos", "vitorias", "empates", "derrotas", "partidas", "posicao", "golsPro", "golsContra", "saldo", "cartoesA", "cartoesV"])
    df.to_csv(str(p)+"\\database\\dados.csv", sep=";")

    updateBD()