from PIL import Image
import matplotlib.pyplot as plt


def converter_imagem(caminho_entrada, caminho_saida):
    try:
        # Abrir imagem original
        imagem = Image.open(caminho_entrada)

        # Converter para JPG (remove transparência se necessário)
        if imagem.mode in ('RGBA', 'LA'):
            imagem = imagem.convert('RGB')  # [[3]][[7]]

        # Salvar imagem convertida
        imagem.save(caminho_saida, 'JPEG', quality=90)
        print(f"Imagem salva em: {caminho_saida}")

        # Mostrar antes/depois
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.title("Original")
        plt.imshow(imagem)

        plt.subplot(1, 2, 2)
        plt.title("Convertida")
        plt.imshow(Image.open(caminho_saida))
        plt.show()

    except Exception as e:
        print(f"Erro: {e}")


# Exemplo de uso
converter_imagem('imagem.png', 'imagem_convertida.jpg')
