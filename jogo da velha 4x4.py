#esse vai ser o tabuleiro do jogo
tabuleiro = ["-","-","-","-",
         "-","-","-","-",
         "-","-","-","-",
         "-","-","-","-"]
#primeiro jogador sera o "x"
jogador_atual = "x"
ganhador=None
contador_de_jogadas=0
jogadas_passadas=[]

#definindo uma funcao para imprimir o tabuleiro
def imprimir_tabuleiro():
    print (tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2] + " | " + tabuleiro[3] )
    print (tabuleiro[4] + " | " + tabuleiro[5] + " | " + tabuleiro[6] + " | " + tabuleiro[7])
    print (tabuleiro[8] + " | " + tabuleiro[9] + " | " + tabuleiro[10] + " | " + tabuleiro[11])
    print (tabuleiro[12] + " | " + tabuleiro[13] + " | " + tabuleiro[14] + " | " + tabuleiro[15])

#definindo uma funcao para mudar o jogador de 'x' para 'o'
def muda_jogador(jogador):
    jogador_atual
    if jogador=="x":
        return "o"
    else:
        return "x"

#definindo uma funcao para checar se tem um vencedor nas fileiras
def checar_fileira():

    if (tabuleiro[0]==tabuleiro[1]==tabuleiro[2]=="x" or tabuleiro[1]==tabuleiro[2]==tabuleiro[3]=="x"  or tabuleiro[4]==tabuleiro[5]==tabuleiro[6]=="x" or tabuleiro[5]==tabuleiro[6]==tabuleiro[7]=="x" or
            tabuleiro[8]==tabuleiro[9]==tabuleiro[10]=="x" or tabuleiro[9]==tabuleiro[10]==tabuleiro[11]=="x" or tabuleiro[12]==tabuleiro[13]==tabuleiro[14]=="x" or tabuleiro[13]==tabuleiro[14]==tabuleiro[15]=="x") :
        return 'x'
        
    elif (tabuleiro[0]==tabuleiro[1]==tabuleiro[2]=="o" or tabuleiro[1]==tabuleiro[2]==tabuleiro[3]=="o"  or tabuleiro[4]==tabuleiro[5]==tabuleiro[6]=="o" or tabuleiro[5]==tabuleiro[6]==tabuleiro[7]=="o" or
            tabuleiro[8]==tabuleiro[9]==tabuleiro[10]=="o" or tabuleiro[9]==tabuleiro[10]==tabuleiro[11]=="o" or tabuleiro[12]==tabuleiro[13]==tabuleiro[14]=="o" or tabuleiro[13]==tabuleiro[14]==tabuleiro[15]=="o"):
        return "o"
    else:
        return None

#definindo uma funcao para checar se tem um vencedor nas colunas
def checar_diagonais():
    if (tabuleiro[0]==tabuleiro[5]==tabuleiro[10]=="x" or tabuleiro[5]==tabuleiro[10]==tabuleiro[15]=="x" or tabuleiro[1]==tabuleiro[6]==tabuleiro[11]=="x" or tabuleiro[4]==tabuleiro[9]==tabuleiro[14]=="x" 
        or tabuleiro[2]==tabuleiro[5]==tabuleiro[8]=="x" or tabuleiro[7]==tabuleiro[10]==tabuleiro[13]=="x" or tabuleiro[3]==tabuleiro[6]==tabuleiro[9]=="x" or tabuleiro[6]==tabuleiro[9]==tabuleiro[12]=="x"):
        return "x"
    elif (tabuleiro[0]==tabuleiro[5]==tabuleiro[10]=="o" or tabuleiro[5]==tabuleiro[10]==tabuleiro[15]=="o" or tabuleiro[1]==tabuleiro[6]==tabuleiro[11]=="o" or tabuleiro[4]==tabuleiro[9]==tabuleiro[14]=="o" 
        or tabuleiro[2]==tabuleiro[5]==tabuleiro[8]=="o" or tabuleiro[7]==tabuleiro[10]==tabuleiro[13]=="o" or tabuleiro[3]==tabuleiro[6]==tabuleiro[9]=="o" or tabuleiro[6]==tabuleiro[9]==tabuleiro[12]=="o"):
        return "o"
    else:
        return None

#definindo uma funcao para checar se tem um vencedor nas diagonais        
def checar_colunas():
    if (tabuleiro[0]==tabuleiro[4]==tabuleiro[8]=="x" or tabuleiro[4]==tabuleiro[8]==tabuleiro[12]=="x" or tabuleiro[1]==tabuleiro[5]==tabuleiro[9]=="x" or tabuleiro[5]==tabuleiro[9]==tabuleiro[13]=="x" or
        tabuleiro[2]==tabuleiro[6]==tabuleiro[10]=="x" or tabuleiro[6]==tabuleiro[10]==tabuleiro[14]=="x" or tabuleiro[3]==tabuleiro[7]==tabuleiro[11]=="x" or tabuleiro[7]==tabuleiro[11]==tabuleiro[15]=="x"):
        return "x"
    elif (tabuleiro[0]==tabuleiro[4]==tabuleiro[8]=="o" or tabuleiro[4]==tabuleiro[8]==tabuleiro[12]=="o" or tabuleiro[1]==tabuleiro[5]==tabuleiro[9]=="o" or tabuleiro[5]==tabuleiro[9]==tabuleiro[13]=="o" or
        tabuleiro[2]==tabuleiro[6]==tabuleiro[10]=="o" or tabuleiro[6]==tabuleiro[10]==tabuleiro[14]=="o" or tabuleiro[3]==tabuleiro[7]==tabuleiro[11]=="o" or tabuleiro[7]==tabuleiro[11]==tabuleiro[15]=="o"):
        return "o"
    else:
        return None

#juntando todas as checagens de vencedor
def checar_ganhador():
    vencedor=checar_fileira()
    if vencedor == None:
        vencedor=checar_colunas()
        if vencedor == None:
           vencedor= checar_diagonais()
    if vencedor == "x":
       return "x"
    elif vencedor == "o":
        return "o"

#nos certificando que se o usuario digitar um dado invalido o programa retornara um erro
def checar_erro(posicao_jogada_str):
    # Ao fazer um Try except, se o usuario nao digitar um numero, ele recebe um aviso dizendo que a posicao e invalida
    try :
        posicao_jogada_int= int (posicao_jogada_str)
        #se o usuario digitar um numero menor que 1 ou maior que 9 ou ainda, uma posicao ja jogada, ele recebera um erro.
        if posicao_jogada_int<1 or posicao_jogada_int>16 :
            print ("essa nao e uma posicao valida, use o numero de 1-16")
            return False
        elif posicao_jogada_str in jogadas_passadas :
            print ('essa posicao ja foi jogada, escolha outra.')
            return False
        else:
            return posicao_jogada_int
    except :
        print ("essa nao e uma posicao valida, use o numero de 1-16")
        return False

    


#imprimir posicoes do tabuleiro
def posicoes_do_tabuleiro():
    print('1-2-3-4')
    print('5-6-7-8')
    print('9-10-11-12')
    print('13-14-15-16')

#fazendo um loop para o jogo prosseguir enquanto nao houve vencedor ate ser decretado um empate
while ganhador==None:
    posicoes_do_tabuleiro()
    imprimir_tabuleiro()
    posicao_jogada = input("escolha uma posicao:")
    posicao_jogada_int=checar_erro(posicao_jogada)
    if posicao_jogada_int==False:
        continue
    tabuleiro[posicao_jogada_int-1]=jogador_atual
    #criamos uma lista com todas as jogadas para que o usuario nao possa jogar em uma posicao ja jogada
    jogadas_passadas.append(posicao_jogada)
    
    ganhador=checar_ganhador()
    if ganhador !=None:
         imprimir_tabuleiro()
         print ("o ganhardor e " + ganhador)
    #A cada jogada sem vencedor, o contador de jogadas aumenta 1 para que possamos contabilizar um empate
    contador_de_jogadas=contador_de_jogadas+1
    #se o numero de jogadas chegar a 9 e nao houver vencedor, isso nos retorna um empate
    if contador_de_jogadas==16:
        if ganhador==None:
            print("deu empate.")
            break

    jogador_atual=muda_jogador(jogador_atual)
