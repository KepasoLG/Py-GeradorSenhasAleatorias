import random
import string

def gerar_senha(comprimento=12, incluir_numeros=True, incluir_caracteres_especiais=True):
    # Definindo os caracteres possíveis para a senha
    caracteres = string.ascii_letters  # Letras maiúsculas e minúsculas
    if incluir_numeros:
        caracteres += string.digits  # Números de 0 a 9
    if incluir_caracteres_especiais:
        caracteres += string.punctuation  # Caracteres especiais (como @, #, $, etc.)
    
    # Gerando a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    
    return senha

# Função principal
def main():
    print("Gerador de Senhas Aleatórias")
    
    comprimento = int(input("Digite o comprimento da senha desejada: "))
    incluir_numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
    incluir_caracteres_especiais = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'

    senha = gerar_senha(comprimento, incluir_numeros, incluir_caracteres_especiais)
    
    print("\nSua senha gerada é:", senha)

if __name__ == "__main__":
    main()
