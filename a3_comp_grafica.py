import cv2
import numpy as np
import urllib.request

# Faz o dowload da imagem
def imagem_baixada(url, nome_arquivo):
    urllib.request.urlretrieve(url, nome_arquivo)

# Faz a aplicação da translação
def aplicando_translacao(image, tx, ty):
    altura, largura, _ = image.shape
    matriz_translacao = np.float32([[1, 0, tx], [0, 1, ty]])
    imagem_translacao = cv2.warpAffine(image, matriz_translacao, (largura, altura))
    return imagem_translacao

# Aplica a rotação na imagem 
def aplicando_rotacao(image, angulo):
    altura, largura, _ = image.shape
    matriz_rotacao = cv2.getRotationMatrix2D((largura / 2, altura / 2), angulo, 1)
    imagem_rotacionada = cv2.warpAffine(image, matriz_rotacao, (largura, altura))
    return imagem_rotacionada

# Aplica  o espelhamento
def aplicando_espelhamento(image, espelhamento_valor):
    imagem_espelhada = cv2.flip(image, espelhamento_valor)
    return imagem_espelhada

# Aplica o filtro de cor
def aplicando_filtro_cor(image, cor, opacidade):
    cor_filtro = np.zeros_like(image)
    cor_filtro[:,:] = cor[::-1]
    imagem_Cfiltro = cv2.addWeighted(image, 1 - opacidade, cor_filtro, opacidade, 0)
    return imagem_Cfiltro

# Url da imagem utilizada, e salvando ela para usar posteriormente
image_url = "data:image/jpeg;base64,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"
nome_arquivo = "imagem_original.jpg"
imagem_baixada(image_url, nome_arquivo)
imagem_original = cv2.imread(nome_arquivo)

# Crição de um loop para usar o menu de escolhas
while True:
    print("\nEscolha uma das transformação abaixo:")
    print("1. Translação")
    print("2. Rotação")
    print("3. Espelhamento Horizontal")
    print("4. Espelhamento Vertical")
    print("5. Aplicar Filtro de Cor")
    print("0. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "0":
        break
    elif escolha == "1":
        tx = int(input("Digite o valor de translação em x: "))
        ty = int(input("Digite o valor de translação em y: "))
        imagem_transformada = aplicando_translacao(imagem_original, tx, ty)
    elif escolha == "2":
        angulo = float(input("Digite o ângulo de rotação: "))
        imagem_transformada = aplicando_rotacao(imagem_original, angulo)
    elif escolha == "3":
        imagem_transformada = aplicando_espelhamento(imagem_original, 1)
    elif escolha == "4":
        imagem_transformada = aplicando_espelhamento(imagem_original, 0)
    elif escolha == "5":
        cor = tuple(map(int, input("Digite a cor (R G B): ").split()))
        opacidade = float(input("Digite a opacidade (entre 0 e 1): "))
        imagem_transformada = aplicando_filtro_cor(imagem_original, cor, opacidade)
    else:
        print("Opção inválida. Tente novamente.")
        continue
# Mostrarando a imagem transformada após as modificações
    cv2.imshow("Imagem Transformada", imagem_transformada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("Programa encerrado.")
