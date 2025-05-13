# Limak is going to participate in a contest on the last day of the 2016. The contest will start at 20:00 and will last four hours, exactly until midnight. There will be n problems, sorted by difficulty, i.e. problem 1 is the easiest and problem n is the hardest. Limak knows it will take him 5·i minutes to solve the i-th problem.

# Limak's friends organize a New Year's Eve party and Limak wants to be there at midnight or earlier. He needs k minutes to get there from his house, where he will participate in the contest first.

# How many problems can Limak solve if he wants to make it to the party?

# Input
# The only line of the input contains two integers n and k (1 ≤ n ≤ 10, 1 ≤ k ≤ 240) — the number of the problems in the contest and the number of minutes Limak needs to get to the party from his house.

# Output
# Print one integer, denoting the maximum possible number of problems Limak can solve so that he could get to the party at midnight or earlier.

q, minuto = map(int, input().split())
tempo = 240 - minuto
tempo_questoes = 5
i = 1
total_questoes = 0
while tempo_questoes <= tempo:
    if total_questoes == q: break
    i += 1
    tempo_questoes += 5*i
    total_questoes += 1
print(total_questoes)