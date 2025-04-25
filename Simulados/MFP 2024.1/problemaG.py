# Sonic and Amy were watching the Olympics basketball finals. As Sonic is really detailed, he registered each score of the match in his notebook of annotations. For example, if team Time 1 scored with a free throw, he wrote "Time 1 +1". In the same way, if team Time 2 scored a triple, he registered "Time 2 +3".

# Until the end of the match, everything was fine. However, at the end of the game, there was a problem with the scoreboard, and the teams scores were lost. Happily for the organizers, Sonic had every detail of the game written in his notebook.

# Given the content of Sonic's notebook, what would be the result of the match between Time 1 and Time 2?

# Input
# The first line of input contains an integer n(1≤n≤100).

# Then follow n lines, each in the format "Time t+k" (without quotes), which indicates that Time t made a basket of k points (t∈{1,2}, k∈{1,2,3}).

# Output
# Print a line in the format "p1 x p2" (without quotes), where p1 represents Time 1's score and p2 represents Time 2's score. Note that there is a space before and a space after the "x".

#pontuacao[1] para saber qual time ganhou
#int(list(pontuacao[2])[1]) para pegar o valor do ponto
time1 = 0
time2 = 0
jogadas = int(input())
for _ in range(jogadas):
    pontuacao = input().split()
    if pontuacao[1] == "1":
        time1 += int(list(pontuacao[2])[1])
    else:
        time2 += int(list(pontuacao[2])[1])
print(f"{time1} x {time2}")





