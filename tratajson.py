import json
import numpy as np
import pandas as pd
from datetime import datetime
from flask import jsonify

def jsonPrepare(data):
    # dicionarios para dados e indice
    idx_skill = []
    dados = []

    #tamanho de experiencias
    len_data = len(data['freelance']['professionalExperiences'])

    # para para cada experiencia varre os skills
    for i in range(len_data):
        # tamanho dos skills
        len_jobs = len(data['freelance']['professionalExperiences'][i]['skills'])

        # captura informações de cada skill
        for k in range(len_jobs):
            id_skill = data['freelance']['professionalExperiences'][k]['skills'][i]['id']
            name = data['freelance']['professionalExperiences'][k]['skills'][i]['name']

            # faz tratamento das datas
            id_freelance = int(data['freelance']['id'])
            startDate = data['freelance']['professionalExperiences'][k]['startDate']
            startDate = datetime.strptime(startDate[0:10], '%Y-%m-%d')
            endDate = data['freelance']['professionalExperiences'][k]['endDate']
            endDate = datetime.strptime(endDate[0:10], '%Y-%m-%d')

            # cria duas bases com as informações um indice dos ids das skill
            # outro dicionario com todas informaçoes
            idx_skill.append(id_skill)
            dados.append((endDate, startDate, name, id_skill, id_freelance))

    # converte ids das skills em unicos
    idx_skill = np.unique(idx_skill)

    # cria um dataset com dos dados
    df = pd.DataFrame(dados, columns=["data_f", "data_i", "skill", "id_skill", "id"])

    # varre o dataset e para gerar dados unicos
    output = []
    for j in idx_skill:
        #cria um dataset so com skill do loop
        df1 = df[df['id_skill'] == j]

        # primeira data do skill
        data_i = df1['data_i'].min()
        # ultima data do skill
        data_f = df1['data_f'].max()

        # calcula periodo em meses
        durationInMonths = (data_f - data_i)
        durationInMonths = int(durationInMonths.days / 30)

        # pega novamento o id do skill agora filtrado no laço
        id_skill: int = int(j)

        # tramento do nome do skill
        name = np.array2string(df1['skill'].unique())
        name = name.split('\'')
        name = name[1]

        # para cada item do laço guarda em um dicionario
        output.append({'id_skill': id_skill, 'name': name, 'durationInMonths': durationInMonths})

    # cria o cabeçalho do dicionario e concatena para criar o arquivo
    jsonfile = dict()
    jsonfile['computedSkills'] = output
    jsonfile['id'] = data['freelance']['id']
    return jsonify(jsonfile)