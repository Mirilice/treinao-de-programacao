# Considere as definições abaixo:

# Uma palavra é uma sequência de letras consecutivas.
# Um texto é um conjunto de palavras separadas pelo caractere espaço em branco.
# Você foi contratado pela empresa Booble para escrever um programa que, dados uma letra e um texto, determina a porcentagem de palavras do texto que contém a letra dada.

# Entrada
# A primeira linha da entrada contém um único caractere, a letra de interesse na pesquisa. A segunda linha contém um texto, como definido acima. O texto é composto apenas por letras minúsculas e o caractere espaço em branco, o texto é formado por no mínimo um caractere, e no máximo 1000 caracteres, o texto não contém dois espaços em branco consecutivos.

# Saída
# Seu programa deve produzir uma única linha, contendo um único número real, a porcentagem de palavras do texto que contêm a letra dada, com precisão de uma casa decimal.

letra = input()
texto = input().split()
quant_palavra = len(texto)
quant_letra = 0
for palavra in texto:
    for letras in palavra:
        if letras == letra:
            quant_letra+=1 
            break
porcentagem = (quant_letra/quant_palavra)*100
print(f"{porcentagem:.1f}")