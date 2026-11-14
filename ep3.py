"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : João Lucas Rodrigues
  NUSP : -------
  Turma: 2020-222
  Prof.: Paulo Andre Vechiatto de Miranda

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  comando break e continue: https://panda.ime.usp.br/pensepy/static/pensepy/07-Iteracao/maisiteracao.html
  
  em especial o trecho: "Agora, também temos break para sair de um laço (mas não da função), e continue para abandonar a iteração atual do laço sem terminar o laço."
  
"""

import math

DELTA_T = 0.1
GRAVIDADE = 2

# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente neste bloco as funções obrigatórias do EP3.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================

def leArquivo(nomeArquivo = 'entrada.txt'):
    '''
    Esta função lê um arquivo ('entrada.txt' por default) e
    retorna uma lista de listas.
    Entrada: arquivo cujo nome está armazenado em nomeArquivo.
             Por default, é 'entrada.txt'
    Saída: uma lista de listas, onde o primeiro elemento é uma
           lista de inteiros [m, n] (dimensões da matriz) e os
           elementos subsequentes são listas que representam as
           característica lidas dos Pokémons na forma:
                [nome, raio, x, y]
    '''
    arquivo = open(nomeArquivo, "r")
    dim = arquivo.readline()
    dimensao_matriz = dim.split() #lista contendo as dimensoes da matriz 
    A = [dimensao_matriz] #lista de listas na qual guardaremos todas as informacoes sobre os arquivos de texto
    info_pok = arquivo.readlines() #informacoes relevantes dos pokemons
    carac_pokemon = []
    for i in range(len(info_pok)):
        dado = info_pok[i].split() #separando os dados 
        b = 3 # contador auxiliar para varrer a lista do tipo [nome, raio, x, y] e transformar tudo menos o nome de string para inteiro
        while b > 0:
            dado[b] = int(dado[b]) #transformando r, x e y em numeros inteiros 
            b = b - 1
        carac_pokemon = carac_pokemon + [dado] #fazendo a lista  q contem as caracteristicas de pokemons, nome raio x y
    
    A.append(carac_pokemon)
    #adicionando a lista que contem a dimensao da matriz
    arquivo.close()
    return A


def criaMatriz(m, n):
    '''
    Esta função cria e retorna uma lista de listas.
    Entrada: dois inteiros que representam o número de linhas e
             o número de colunas da matriz.
    Saída: uma lista de m listas, cada uma com n elementos, todos
           inicializados com zeros.
    '''
    M = [] #matriz inicialmente vazia
    for i in range(int(m)):
        l = [] # lista que representa as linhas da matriz
        for j in range(int(n)):
            l.append(0) #adicionando os 0 representantes as colunas a uma linha da matriz
        M.append(l) # adicionando essa linha de n elementos em nossa matriz M 
        
    return M


def populaMatriz(matriz, pokemons):
    '''
    Esta função recebe uma matriz e uma lista contendo listas que
    representam os pokémons na forma [nome, raio, x, y] e preenche-a
    os pokémons conforme a representação retangular considerando os
    raios da representação.
    Entrada: matriz representada por uma lista de listas
    Saída: A matriz fornecida é modificada.
    '''
    id = 0 #id inicial para identificar os pokemons
    for i in range(len(pokemons)):
        preenchePokemon(matriz, id, pokemons[i][2], pokemons[i][3], pokemons[i][1])
        id = id + 1
        
    return matriz
   


def preenchePokemon(matriz, id, x, y, raio):
    '''
    Esta função é auxiliar da função populaMatriz. Ela insere
    um Pokémon na matriz de acordo com sua representação retangular
    baseada no raio ao redor do ponto central (x,y)
    Entrada: matriz representada por uma lista de listas
             id é o número a preencher a matriz; para o
             primeiro pokémon na lista (de índice zero),
             usa-se 1 e assim subsequentemente.
             x,y são as coordenadas do ponto central
             raio é a distância a ser guardada a partir do
             ponto central.
    Saída: A matriz fornecida é modificada.
    '''

    for i in range(y - raio, y + raio+1):
        for j in range(x - raio, x + raio+1):
                matriz[i][j] = id + 1 #trocando o valor dos termos que pertencem a um quadrado de lado 2*raio centrado em y,x
    return matriz


def removePokemon(matriz, id, pokemons):
    '''
    Esta função recebe uma matriz, o numeral que representa o pokémon
    a ser removido da matriz (id) e a lista contendo as listas que
    representam pokémons, substituindo os numerais id por zero
    Entrada: matriz representada por uma lista de listas;
             id é o número a preencher a matriz, para o
             primeiro pokémon na lista (de índice zero),
             usa-se 1 e assim subsequentemente;
             pokemons lista contendo as listas que representam pokémons.
    Saída: A matriz fornecida é modificada.
    '''
    poke_info = pokemons[id] #lista contendo informacoes a respeito do pokemon a ser removido da matriz
    r = poke_info[1] #raio do pokemon a ser retirado
    lin = poke_info[3] # linha em que esta o pokemon
    col = poke_info[2] # coluna em que esta o pokemon
    for linha in range(lin-r, lin + r + 1):
        for coluna in range(col - r, col + r + 1):
            matriz[linha][coluna] = 0 #trocando o valor dos termos que pertencem a um quadrado de lado 2r
            
    
    return matriz


def imprimeMatriz(matriz):
    '''
    Esta função imprime a matriz dada.
    Note que a matriz deve ser impressa com espelhamento vertical, 
    pois a primeira linha representa o chão.
    Entrada: matriz representada por uma lista de listas.
    '''
    
    a = len(matriz)
    
    while a > 0:
        l = matriz[a-1] #linha da matriz, que comeca na ultima linha e vem decrescendo
        for i in range(len(l)):
            if matriz[a-1][i] == 0:
                print(".", end="")
            else:
                print(matriz[a-1][i], end="")
        a = a - 1 #decrescendo o numero da linha
        print()
        
    return None


def atualizaPosicao(x, y, vx, vy, dt=DELTA_T):
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    '''
    x = (x + vx*dt) #atualizacao da posicao 
    y = (y + vy*dt - ((GRAVIDADE)/2) * (dt**2))
    return [x,y]


def atualizaVelocidade(vx, vy, dt=DELTA_T):
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    '''
    vx = vx
    vy = vy - (GRAVIDADE)*dt 
    return [vx,vy]


def grau2Radiano(theta):
    '''
    Esta função converte o ângulo theta em graus para radianos.
    Entrada: ângulo theta.
    Saída: ângulo theta em radianos.
    '''
    theta_rad = (theta * math.pi)/(180)
    return theta_rad


def copiaMatriz(matriz, m, n):
    '''
    Esta funcao tem como entrada uma matriz juntamente com as dimensoes da mesma e cria uma copia da matriz de entrada
    '''
    a = len(matriz)
    P = criaMatriz(m, n) #criando uma matriz na mesma dimensao que a matriz de entrada para copiar seus valores
    for i in range(a):
        for j in range (len(matriz[a-1])): #varrendo a matriz de entrada e copiando seus termos para outra matriz
            P[i][j] = matriz[i][j]
    return P


def main():
    nome = input("Digite o nome do arquivo: ")
    N = int(input("Digite o numero N de pokebolas: "))
    x_t = int(input("Digite a coordenada x do treinador: "))
    info = leArquivo(nome) #lendo arquivo e pegando as informacoes sobre os pokemons
    M = criaMatriz( info[0][0], info[0][1]) #criando a matriz na dimensao certa m x n
    pokemons = info[1] #lista que contem as listas contendo as informacoes dos pokemons
    num_poke = len(pokemons)  #numero de pokemons
    M = populaMatriz(M,pokemons) #populando a matriz com os pokemons
    
    while N>0 and num_poke > 0:
        
        x_p = x_t #posicoes iniciais da pokebola
        y_p = 0
        x = round(x_p) #valores inteiros das posicoes da pokebola
        y = round(y_p)
        print("pokebolas disponiveis = ",N)
        print("Estado atual do jogo: ")
        M[0][x_t] = "T" 
        P = copiaMatriz(M, int(info[0][0]), int(info[0][1]) ) #uma copia da matriz original M para que seja alterada a cada iteracao sem que altere a matriz original
        imprimeMatriz(M)
        vlancamento = int(input("Digite a velocidade de lancamento em m/s: "))
        theta = int(input("Digite o angulo de lancamento em graus: "))
        vx_p = vlancamento * math.cos(grau2Radiano(theta))
        vy_p = vlancamento * math.sin(grau2Radiano(theta))
        print("Representacao grafica do lancamento: ")
        Pegou = True #boleano que diz se houve captura ou nao de pokemon 
        while y >= 0: #condicoes de parada do programa
        
            
            if x >= 0 or x <= int(info[0][1]) - 1:  # x da pokebola no intervalo (0,n) dentro dos limites verticais da matriz
                Pegou = False
            
                if (x == 0 and vx_p < 0) or (x == int(info[0][1]) - 1 and vx_p > 0): #pokebola no limite da matriz, prestes a sair da mesma
                    imprimeMatriz(P)
                    print("O lancamento nao capturou pokemon algum")
                    break
                
                else:
                
                
                    s = atualizaPosicao(x_p, y_p, vx_p, vy_p, dt=DELTA_T)
                    v = atualizaVelocidade(vx_p, vy_p, dt=DELTA_T)
                    x_p = s[0] #posicoes da pokebola atualizadas apos dt segundos
                    y_p = s[1] 
                    x = round(x_p) #posicao da pokebola arredondada para numeros inteiros
                    y = round(y_p)
                    vx_p = v[0]
                    vy_p = v[1]
                    
                    if 0 <= x <= int(info[0][1]) - 1 : # se o x esta nos limites da matriz apos atualizacao
    
                        if y > int(info[0][0]) - 1 : #pokebola numa posicao fora da matriz no eixo y
                            continue
                        
                        elif y < 0:
                            imprimeMatriz(P)
                            print("O lancamento nao capturou pokemon algum")
                            break
                            
                        elif M[y][x] == 0: #nao atingiu nenhum pokemon, passando por uma posicao vazia 
                            P[y][x] = "o"
                    
                        elif (M[y][x] != 0 and M[y][x] != "T" and M[y][x] != "o"): #pokebola atingiu algum pokemon
                            Pegou = True
                            num = M[y][x] - 1 #numero do pokemon na lista de pokemons, id do pokemon
                            P[y][x] = "o"
                            imprimeMatriz(P)
                            removePokemon(M, num, pokemons) #retirando o pokemon da matriz
                            num_poke = num_poke - 1
                            M[0][x_t] = 0 #retirando o treinador da posicao anterior 
                            x_t = x  #nova posicao da linha na matriz do treinador, posicao x na qual o pokemon foi capturado
                            print("Um",pokemons[num][0],"foi capturado!")
                            break
                    else:
                        imprimeMatriz(P)
                        print("O lancamento nao capturou pokemon algum ")
                        break
                      
                        
                        
           
                  
        
        N = N - 1
        if Pegou == False and N>0 and num_poke > 0:
            M[0][x_t] = 0
            x_t = int(input("Digite a coordenada x do treinador: "))
        
        if num_poke == 0 and N >= 0:
            print("Parabens! Todos pokemons foram capturados")
            
        elif N ==0 and num_poke > 0:
            print("Jogo encerrado")

 
main()