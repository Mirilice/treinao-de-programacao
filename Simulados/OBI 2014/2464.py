# Dimas é um renomado investigador de roubos a antiguidades e obras de arte, que sempre é chamado para casos intrigantes que necessitam de bastante trabalho mental. Desta vez, o quadro que sumiu de um conhecido museu na França foi a Donalisa, do pintor Leonardo da Silva. Este é um caso bastante especial, visto que o ladrão deixou uma frase escrita na parede, aparentemente criptografada. Que desafio para Dimas! É que ele não tem muito conhecimento nessa área de criptografia. Porém, ele usou de suas excelentes observações e conseguiu perceber que a frase foi escrita através de alguma permutação inversível do alfabeto.

# Uma permutação inversível do alfabeto é apenas uma troca entre suas letras, duas a duas. Por exemplo, todo “a” será trocado por “m” e, portanto, todo “m” será trocado por “a”. Dessa forma, veja que dado um texto original, se aplicarmos a permutação, teremos uma frase criptografada; e se aplicarmos a mesma permutação novamente, teremos o texto original recuperado!

# Apesar de parecer fácil, a tradução se tornou uma tarefa difícil, já que a frase é bastante longa. É por isso que Dimas resolveu pedir sua ajuda, um exímio programador, para traduzir a frase criptografada, recuperando o texto original, e resolver o mistério!

# Entrada
# A primeira linha da entrada contém uma sequência de 26 letras minúsculas distintas, representando a permutação inversível usada na frase criptografada. A permutação é a seguinte: a letra “a” é trocada pela primeira letra dessa sequência; a letra “b” é trocada pela segunda letra dessa sequência; a letra “c” pela terceira; e assim por diante, seguindo a sequência padrão do alfabeto: abcdefghijklmnopqrstuvwxyz. A segunda linha da entrada consiste de uma frase criptografada, contendo apenas letras minúsculas (a frase criptografada não excede 104 caracteres).

# Saída
# Seu programa deve imprimir o texto original, de acordo com a permutação fornecida.

original = "abcdefghijklmnopqrstuvwxyz"
permutacao = input()
frase = input()
palavra_descoberta = ""
for letra in frase:
    posicao_letra = permutacao.index(letra)
    palavra_descoberta += original[posicao_letra]
print(palavra_descoberta)
    
