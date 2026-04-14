import cv2
import numpy as np
import pandas as pd

# Carrega a imagem
imagem = cv2.imread('Projeto1/imagemParaSeparar.jpg')

if imagem is None:
    print("Erro: Não foi possível carregar a imagem.")
else:

    canais = cv2.split(imagem) #em BGR
    azul, verde, vermelho = canais
    #azul[azul == 255] = 0
    imagem_azul = cv2.merge([azul, np.zeros_like(azul), np.zeros_like(azul)])
    imagem_verde = cv2.merge([np.zeros_like(verde), verde, np.zeros_like(verde)])
    imagem_vermelho = cv2.merge([np.zeros_like(vermelho), np.zeros_like(vermelho), vermelho])

    pd.DataFrame(azul).to_csv('canal_azul.csv', index=False, header=False)
    pd.DataFrame(verde).to_csv('canal_verde.csv', index=False, header=False)
    pd.DataFrame(vermelho).to_csv('canal_vermelho.csv', index=False, header=False)


    cv2.imshow('Canal Azul', azul)
    cv2.waitKey(0)
    cv2.imshow('Canal verde', verde)
    cv2.waitKey(0)
    cv2.imshow('Canal vermelho', vermelho)
    cv2.waitKey(0)


    # cv2.imshow('Canal Azul', imagem_azul)
    # cv2.waitKey(0)
    
    # cv2.imshow('Canal verde', imagem_verde)
    # cv2.waitKey(0)

    # cv2.imshow('canal vermelho', imagem_vermelho)
    # cv2.waitKey(0)


    print("Arquivos CSV salvos com sucesso!")