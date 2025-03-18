import random
import string

# Função para gerar senhas fortes
def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation  # Letras, números e símbolos [[3]]
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))  # Gera a senha aleatória [[4]]
    return senha

# Função principal
def main():
    print("=== GERADOR DE SENHAS FORTES ===")
    try:
        tamanho = int(input("Digite o tamanho da senha (padrão: 12): "))
        if tamanho <= 0:
            raise ValueError("O tamanho deve ser maior que zero.")
    except ValueError:
        print("Usando tamanho padrão: 12")
        tamanho = 12

    senha = gerar_senha(tamanho)
    print(f"\nSenha gerada: {senha}")
    print("Copie a senha e use onde precisar!")

# Executa o programa
if __name__ == "__main__":
    main()
