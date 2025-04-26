# Amy Rose está em uma missão secreta para derrotar Eggman. Como parte de seu plano, ela teve que se
# separar de Sonic, e agora eles podem se comunicar apenas através de código Morse. Porém, como toda
# forma de comunicacão, é possível que as mensagens sejam interpretadas de forma errada, gerando grande
# confusão.
# Para lidar com isso, Amy desenvolveu um rebuscado esquema de segurança. Sabemos que as mensagens
# em Morse consistem de traços e pontos. Como amante da ciência da computação, Amy representa traços
# por um 1 e pontos por um 0, tendo a mensagem em binário. Foi combinado que toda mensagem teria 7
# dígitos binários e por fim um bit de segurança. Esse bit é igual a 0 se a quantidade de 1’s na mensagem
# for par e 1 caso contrário.
# Dessa forma, se o bit de segurança for 0 e o código da mensagem tem um número ímpar de bits 1, então
# com certeza a mensagem foi corrompida. Por outro lado, mesmo que não haja uma contradição na versão
# criptografada, o bit de segurança não garante que a mensagem captada condiz com a original, uma vez
# que pode ocorrer de mais de 1 bit ter sido comprometido.
# Dados os 8 bits (7 da mensagem mais o de segurança) sua tarefa é dizer se a mensagem certamente foi
# corrompida ou se não podemos concluir com certeza.
# Input
# A entrada é dada por 8 inteiros separados por espaço em uma única linha. E garantido que cada inteiro ´
# é ou 0 ou 1.
# Output
# Se você tem certeza que a mensagem foi corrompida, imprima apenas o caracter "S". Caso contrário,
# imprima "N?"(sem aspas).

codigo = input().split()
digitos1 = 0
for i in range(len(codigo)-1):
    if codigo[i] == "1": 
        digitos1+=1 
if (digitos1 % 2 == 0 and codigo[-1] == "0") or (digitos1 % 2 != 0 and codigo[-1] == "1"): 
    print("N?")
else: print("S")