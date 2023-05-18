import random

print("---------------------------------------")
print("Seja bem vindo ao jogo de adivinhação!")
print("---------------------------------------")

numero_secreto = (random.randrange(1,101))
tentativas = 0
pontuacao = 1000

print("Selecione o nível de difículdade")
print("Fácil(1) Médio(2) Difícil(3)")

nivel = int(input("Selecione a difículdade"))

if(nivel == 1):
   tentativas = 20
elif(nivel == 2):
   tentativas = 10
else:
   tentativas = 5
for rodada in range(1, tentativas +1):
 print("tentativa {} de {}".format(rodada, tentativas))
 chute_string = input("Diga qual é o número misterioso: ")
 print("Você digitou: ", chute_string)
 chute = int(chute_string)
 if(chute < 1 or chute >100):
    print("Você deve digitar um número entre 1 e 100")
    continue
 acertou = chute == numero_secreto
 maior = chute > numero_secreto
 if(acertou):
    print("Parabéns, você acertou e fez {} pontos!".format(pontuacao))
    break
 elif(maior):
    print("Você errou, seu chute é maior do que o número secreto")
 else:
    print("Você errou, seu número é menor do que o número secreto")

                  #Retorna um número desconsiderando o sinal  
pontos_perdidos = abs(numero_secreto) -  chute
pontuacao = pontuacao - pontos_perdidos

print("Fim de jogo!")