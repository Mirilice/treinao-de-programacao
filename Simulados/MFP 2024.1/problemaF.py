# During the Olympiads of this year, Amy was responsible for updating the scores of her country. In order to do this, she asked Sonic to help her know which were the victories of her country.

# However, her country values some medals more than others. The score of each medal is the following:

# Victory in programming (after all, this is an Olympic sport): 8 points
# Victory in volleyball (after all, this is the coolest sport): 4 points
# Victory in soccer (after all, this is the country of soccer): 2 points
# Victory in race (after all, we have The Sonic): 1 point
# Sonic was kind of lost with the amount of matches and, instead of giving to Amy which sport they won, he returned the sum of points.

# Given the sum of the points, help Amy to count how many different sports they won.

# Input
# The input is an integer number N(1≤N≤15), the sum of the points returned by Sonic.

# It is guaranteed that victory in each modality is unique.

# Output
# The output must be an integer, representing the number of sports in which Amy's country won medals.

#programacao - 8 
#volei - 4
#futebol - 2
#corrida - 1 
total_esportes = 0
pontos = int(input())
i = 3
while pontos > 0:
    if pontos - 2**i >= 0:
        pontos -= 2**i
        total_esportes += 1
    i-=1
print(total_esportes)