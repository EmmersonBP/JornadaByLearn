def media_de_notas(x):
    notas = []
    for i in range(x):
        n = float(input('Informe a {}a nota: '.format(i+1)))
        notas.append(n)

    #print('Notas: ', notas)

    media = sum(notas)/len(notas)
    print("Média: %.2f" %media)
    return media

def verificação_de_Aprovação(y):
    if(y >= 6):
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")

while True:
    numero_de_notas = int(input('Número de notas que deseja calcular a média: '))
    media = media_de_notas(numero_de_notas)
    verificação_de_Aprovação(media)

    op = str(input('\nDeseja calcular outra média?(s/n): '))
    if(op.lower() == 'n'):
        break
print('Operação encerrada!')

brinks = str(input('Cansou de calcular médias? Tá afim de um joguinho?(s/n)'))
if(brinks.lower() == 's'):
    print("\nÓtimo! O jogo é LANÇAMENTO DE DADOS.")
    print("Voçê escolhe um possível resultado para o dado(1 a 6), depois escolho um tamém. Daí vemos quem vence!")
    import random
    while True:
        n_aleatorio = (random.randint (1, 6))   
        escolha_do_robo = (random.randint(1, 6))
        print("\nEu começo! Escolho o número {}.".format(escolha_do_robo))
        sorteio = int(input("Sua vez! Tente adivinhar o número sorteado: "))
            

        if(sorteio == n_aleatorio): 
            print("Parabéns! O número aleatório foi: {}".format(n_aleatorio))
        else:
            print("Que pena, você não acertou :( O número aleatório foi: {}".format(n_aleatorio))

        if(escolha_do_robo == n_aleatorio): 
            print("\nAcertei rsr! O número aleatório foi: {}".format(n_aleatorio))
        else:
            print("Que pena :( Errei! O número aleatório foi: {}".format(n_aleatorio))

        rodada = str(input("Deseja mais uma rodada? "))
        if(rodada.lower() == "n"):
            break
                
    print("Obrigado! Foi muito divertido!")
else:
    print("Tudo bem.Vá descansar!")
    
