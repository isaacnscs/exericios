from random import randint

def entrada ():

    teste = input ("Para fechar o programa, digite SAIR, para continuar, tecle ENTER" "\n")
    teste = teste.upper ()

    if teste == "SAIR":

        exit ()

    else:

        try:

            a = int (input ("Insira o tamanho da lista a ser gerada:"))
            b = int (input ("Insira o numero inicial do intervalo a ser gerado: "))
            c = int (input ("Insira o numero final do intervado a ser gerado: "))

        except:

            print ("\n""#################################")
            print ("Algo deu errado, tente novamente.")
            print ("#################################""\n")

            entrada ()

        return a, b, c

def gerar_lista (): # gerar lista areatória

    "Gerar lista de tamanho <a> contendo numeros aleatórios entre <b> e <c>"

    lista = list ()

    a, b, c = entrada ()

    while len (lista) < a:

        lista.append (randint (b, c))

    return lista

def mapear_posicoes (): # retorna a primeira e ultima posicao de um numero em uma lista

    lista = gerar_lista ()
    lista.sort ()

    posicao_i, posicao_f = (None, None)
    
    try:

        numero = int (input ("Insira o numero a ser analisado: "))

    except:

        print ("\n""#################################")
        print ("Algo deu errado, tente novamente.")
        print ("#################################""\n")

        mapear_posicoes ()

    try:

        ref_1 = 0

        for item in lista:

            if item == numero:

                posicao_i = ref_1

                break

            ref_1 += 1

        ref_2 = ref_1

        for item in lista:

            if lista [ref_2] != numero:

                posicao_f = ref_2 - 1

                break

            ref_2 += 1 

    except:

        if posicao_i == None or posicao_f == None:

            posicao_i, posicao_f = -1, -1

        elif posicao_i == posicao_f:

            posicao_i, posicao_f = -1, -1

    return (posicao_i, posicao_f, lista)

print (mapear_posicoes ())