
def preenche_numeros ():
    numeros = []
    for i in range (1, 51):
        numeros.append(i)
    return numeros

def inicio():
    start_game()
    resp = 's'
    while resp =='s':          
        resp = restart_game ()

def restart_game():
    resp = input('Você gostaria de jogar novamente? (s/n)')
    while resp != 's' and resp != 'n':
        resp = input ('Resposta inválida! Responda novamente com "s" ou "n"!')
    if resp =='s':
        start_game()
        return 's'
    else:
        return 'n'

def par (lista):
    resp = input ('O número que você pensou é par? [s/n]: ')
    pares = []
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in lista:
            if (lista[i-1]%2==0):
                pares.append(lista[i-1])
    else:
        for i in lista:
            if (lista[i-1]%2!=0):
                pares.append(lista[i-1])
    return pares

def div_5 (lista):
    resp = input ('O número que você pensou divide por 5? [s/n]: ')
    div_5 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]%5==0):
                div_5.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]%5!=0):
                div_5.append(lista[i])
    return div_5

def div_3 (lista):
    resp = input ('O número que você pensou divide por 3? [s/n]: ')
    div_3 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]%3==0):
                div_3.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]%3!=0):
                div_3.append(lista[i])
    return div_3

def div_4 (lista):
    resp = input ('O número que você pensou divide por 4? [s/n]: ')
    div_4 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]%4==0):
                div_4.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]%4!=0):
                div_4.append(lista[i])
    return div_4

def div_7 (lista):
    resp = input ('O número que você pensou divide por 7? [s/n]: ')
    div_7 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]%7==0):
                div_7.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]%7!=0):
                div_7.append(lista[i])
    return div_7

def maior_25 (lista):
    resp = input ('O número que você pensou é maior ou igual a 25? [s/n]: ')
    maior25 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=25):
                maior25.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<25):
                maior25.append(lista[i])
    return maior25

def maior_12 (lista):
    resp = input ('O número que você pensou é maior ou igual a 12? [s/n]: ')
    maior12 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=12):
                maior12.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<12):
                maior12.append(lista[i])
    return maior12

def maior_6 (lista):
    resp = input ('O número que você pensou é maior ou igual a 6? [s/n]: ')
    maior6 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=6):
                maior6.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<6):
                maior6.append(lista[i])
    return maior6

def maior_9 (lista):
    resp = input ('O número que você pensou é maior ou igual a 9? [s/n]: ')
    maior9 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=9):
                maior9.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<9):
                maior9.append(lista[i])
    return maior9

def maior_11 (lista):
    resp = input ('O número que você pensou é maior ou igual a 12? [s/n]: ')
    maior11 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=11):
                maior11.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<11):
                maior11.append(lista[i])
    return maior11

def maior_18 (lista):
    resp = input ('O número que você pensou é maior ou igual a 18? [s/n]: ')
    maior18 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=18):
                maior18.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<18):
                maior18.append(lista[i])
    return maior18

def maior_21 (lista):
    resp = input ('O número que você pensou é maior ou igual a 21? [s/n]: ')
    maior21 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=21):
                maior21.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<21):
                maior21.append(lista[i])
    return maior21

def maior_15 (lista):
    resp = input ('O número que você pensou é maior ou igual a 15? [s/n]: ')
    maior15 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=15):
                maior15.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<15):
                maior15.append(lista[i])
    return maior15

def maior_37 (lista):
    resp = input ('O número que você pensou é maior ou igual a 37? [s/n]: ')
    maior37 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=37):
                maior37.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<37):
                maior37.append(lista[i])
    return maior37

def maior_42 (lista):
    resp = input ('O número que você pensou é maior ou igual a 42? [s/n]: ')
    maior42 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=42):
                maior42.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<42):
                maior42.append(lista[i])
    return maior42

def maior_45 (lista):
    resp = input ('O número que você pensou é maior ou igual a 45? [s/n]: ')
    maior45 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=45):
                maior45.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<45):
                maior45.append(lista[i])
    return maior45

def maior_39 (lista):
    resp = input ('O número que você pensou é maior ou igual a 39? [s/n]: ')
    maior39 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=39):
                maior39.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<39):
                maior39.append(lista[i])
    return maior39

def maior_32 (lista):
    resp = input ('O número que você pensou é maior ou igual a 32? [s/n]: ')
    maior32 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=32):
                maior32.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<32):
                maior32.append(lista[i])
    return maior32

def maior_30 (lista):
    resp = input ('O número que você pensou é maior ou igual a 30? [s/n]: ')
    maior30 = []
    size = len(lista)
    while (resp!='s' and resp!='n'):
        resp = input ('Resposta inválida! Digite novamente: ')
    if resp =='s':
        for i in range(size):
            if (lista[i]>=30):
                maior30.append(lista[i])
    else:
        for i in range(size):
            if (lista[i]<30):
                maior30.append(lista[i])
    return maior30

def start_game ():
    print ('PENSE EM UM NÚMERO DE 1 A 50:\n')
    numeros = preenche_numeros()
    conjunto = par (numeros)                
    conjunto = div_5 (conjunto)          
    if  len(conjunto) == 1:
        print ('Fim de jogo! Seu número é:', conjunto)
        return
    conjunto = div_3 (conjunto)         
    if len(conjunto)== 1:
        print ('Fim de jogo! Seu número é:', conjunto)
        return
    conjunto = div_4 (conjunto)         
    if len(conjunto) == 1:
        print ('Fim de jogo! Seu número é:', conjunto)
        return
    conjunto = div_7(conjunto)
    if len(conjunto) == 1:
        print ('Fim de jogo! Seu número é:', conjunto)
        return
    conjunto = maior_25(conjunto)
    if len(conjunto) == 1:
            print ('Fim de jogo! Seu número é:', conjunto)
            return
    if conjunto [0] < 25:
        conjunto = maior_12(conjunto)
        if len(conjunto) == 1:
            print ('Fim de jogo! Seu número é:', conjunto)
            return
        if conjunto [0] < 12:
                conjunto = maior_6(conjunto)
                if len(conjunto) == 1:
                    print ('Fim de jogo! Seu número é:', conjunto)
                    return
        else:
            conjunto = maior_18(conjunto)
            if len(conjunto) == 1:
                    print ('Fim de jogo! Seu número é:', conjunto)
                    return
            if conjunto [0] < 18:
                conjunto = maior_15(conjunto)
                print ('Fim de jogo! Seu número é: ', conjunto)
            else:
                conjunto = maior_21(conjunto)
                print ('Fim de jogo! Seu número é:', conjunto)
    else:
        conjunto = maior_37(conjunto)
        if len(conjunto) == 1:
                print ('Fim de jogo! Seu número é:', conjunto)
                return
        if conjunto [0] <37:
            conjunto = maior_32(conjunto)
            if len(conjunto) == 1:
                print ('Fim de jogo! Seu número é:', conjunto)
                return
            if conjunto[0] <32:
                conjunto = maior_30(conjunto)
                print ('Fim de jogo! O seu número é: ', conjunto)
        else:
            conjunto = maior_42(conjunto)
            if len(conjunto) ==1:
                print ('Fim de jogo! Seu número é:', conjunto)
                return
            if conjunto [0] > 41:
                conjunto = maior_45(conjunto)
                print ('Fim de jogo! Seu número é:', conjunto)
            else: 
                conjunto = maior_39(conjunto)
                print ('Fim de jogo! Seu número é:', conjunto)

inicio ()
