# No oitavo episodio da segunda temporada do seriado The Big Bang Theory, The Lizard-Spock Expansion, Sheldon e Raj discutem qual dos dois é o melhor: o filme Saturn 3 ou a série Deep Space 9. A sugestão de Raj para a resolução do impasse é uma disputa de Pedra-Papel-Tesoura. Contudo, Sheldon argumenta que, se as partes envolvidas se conhecem, entre 75% e 80% das disputas de Pedra-Papel-Tesoura terminam empatadas, e então sugere o Pedra-Papel-Tesoura-Lagarto-Spock.

# As regras do jogo proposto são:

# a tesoura corta o papel;
# o papel embrulha a pedra;
# a pedra esmaga o lagarto;
# o lagarto envenena Spock;
# Spock destrói a tesoura;
# a tesoura decapita o lagarto;
# o lagarto come o papel;
# o papel contesta Spock;
# Spock vaporiza a pedra;
# a pedra quebra a tesoura.
# Embora a situação não se resolva no episódio (ambos escolhem Spock, resultando em um empate), não é difıcil deduzir o que aconteceria se a disputa continuasse. Caso Sheldon vencesse, ele se deleitaria com a vitória, exclamando "Bazinga!"; caso Raj vencesse, ele concluiria que "Raj trapaceou!"; caso o resultado fosse empate, ele exigiria nova partida: "De novo!". Conhecidas as personagens do jogo escolhido por ambos, faça um programa que imprima a provável reação de Sheldon.

# Entrada
# A entrada consiste em uma série de casos de teste. A primeira linha contém um inteiro positivo T (T ≤ 100), que representa o número de casos de teste. Cada caso de teste é representado por uma linha da entrada, contendo as escolhas de Sheldon e Raj, respectivamente, separadas por um espaço em branco. As escolha possíveis são as personagens do jogo: pedra, papel, tesoura, lagarto e Spock.

# Saida
# Para cada caso de teste deverá ser impressa a mensagem "Caso #t: R", onde t é o número do caso de teste (cuja contagem se inicia no número um) e R é uma das três reações possíveis de Sheldon: "Bazinga!", "Raj trapaceou!", ou "De novo!".

n = int(input())
for i in range(n):
    sheldon, raj = input().split()
    if sheldon == raj: print(f"Caso #{i+1}: De novo!")
    elif sheldon == "tesoura" and raj == "papel": print(f"Caso #{i+1}: Bazinga!")
    elif sheldon == "papel" and raj == "pedra": print(f"Caso #{i+1}: Bazinga!")
    elif sheldon == "pedra" and raj == "lagarto": print(f"Caso #{i+1}: Bazinga!")
    elif sheldon == "lagarto" and raj == "Spock": print(f"Caso #{i+1}: Bazinga!")
    elif sheldon == "Spock" and raj == "tesoura": print(f"Caso #{i+1}: Bazinga!")
    elif sheldon == "tesoura" and raj == "lagarto": print(f"Caso #{i+1}: Bazinga!")
    elif sheldon == "lagarto" and raj == "papel": print(f"Caso #{i+1}: Bazinga!")
    elif sheldon == "papel" and raj == "Spock": print(f"Caso #{i+1}: Bazinga!")
    elif sheldon == "Spock" and raj == "pedra": print(f"Caso #{i+1}: Bazinga!")
    elif sheldon == "pedra" and raj == "tesoura": print(f"Caso #{i+1}: Bazinga!")
    else: print(f"Caso #{i+1}: Raj trapaceou!")