# With the arrival of the Olympics, Amy needs to build the best team to compete in the pizza delivery match.

# Being extremely charismatic and prepared, Amy selected N
#  of the best athletes in the pizza carrying event to help her country win a medal.

# The pizza loading competition is simple. The competitors have to deliver p
#  pizzas from the starting point to the end point. That's it, the task is really simple.

# Each member of the team chosen by Amy is numbered from 1 to N. Each of them has a strength Ai, which means that it takes Ai
# seconds to deliver exactly one pizza from the starting point to the end point and return to the starting point again.

# The day of the competition is close. With Amy's ambitious goal to beat the world record, she wants to know the minimum time her team can deliver the p
# pizzas.

# Given the information of each competitor in Amy's team, determine the minimum time for this team to complete the task.

# Input
# The first line of the input consists of two integers N and p that represent the number of members of the team and the number of pizzas that need to be delivered.

# The second line of the input has N integers A1, A2, ..., AN, that represent, in order, the time needed for each competitor to carry a pizza and return to the start.

# Output
# A single integer, the minimum time for the team to complete the task.

quant_competidores, quant_pizzas = map(int, input().split())
tempo_por_competidor = list(map(int, input().split()))
tempo_por_competidor.sort()
tempo_minimo = min(tempo_por_competidor)
total_pizzas = 0
def pizzas_entregues(tempo, tempo_por_competidor, quant_pizzas):
    total_pizzas = 0
    for i in range(len(tempo_por_competidor)):
        total_pizzas+=tempo//tempo_por_competidor[i]
        if total_pizzas >= quant_pizzas:
            return True
    return False
def busca_pizza():
    inicio = 1
    fim = tempo_minimo*quant_pizzas
    while inicio<fim:
        mid = (inicio+fim)//2
        if pizzas_entregues(mid, tempo_por_competidor, quant_pizzas):
            fim = mid #lower bound
            #upper bound, encontrar o maior possível seria o if/else com as condições invertidas
        else: inicio = mid + 1
    return inicio
print(busca_pizza())
        
    
    