def partida ():
    n=int(input("\nQuantas peças ? "))
    m=int(input("limite de peças por jogada ? "))
    c=n
    j=0
    if n % (m+1) !=0:
        print("\nComputador começa!")
        vez=True
        while vez and c>0:
            r=computador_escolhe_jogada(c,m)
            if c-r ==0:
                placar(c,r,i)
                print("\nFim de jogo. O computador ganhou!")
                vez=False
            else:
                i=0
                c=c-r
                placar(c,r,i)
                vez=False
            while not vez:
                v=usuario_escolhe_jogada(c,m)
                if c-v ==0:
                    placar(c,v,i)
                    print("\nFim de jogo. Você ganhou!")
                    j=j+1
                    c=c-v
                    vez=True
                else:
                    c=c-v
                    i=1
                    placar(c,r,i)
                    vez=True
    else:
        print("\nVocê começa!")
        vez=False
        while not vez and c>0:
            r=usuario_escolhe_jogada(c,m)
            if c-r ==0:
                i=1
                placar(c,r,i)
                print("\nFim de jogo. Você ganhou!")
                vez=True
                j=j+1
            else:
                i=1
                c=c-r
                placar(c,r,i)
                vez=True
            while vez:
                v=computador_escolhe_jogada(c,m)
                if c-v==0:
                    print("\nFim de jogo. O computador ganhou!")
                    c=c-v
                    vez=False
                else:
                    c=c-v
                    i=0
                    placar(c,v,i)
                    vez=False
    return j  
    
def placar (c,r,i):
    if i ==1:
        print("\nVocê retirou",r,"peças.")
        print("\nAgora restam",c,"peças no tabuleiro.")
    else:
        print("\nO computador retirou",r,"peças.")
        print("\nAgora restam",c,"peças no tabuleiro.")
   

def computador_escolhe_jogada(c,m):
    r=0
    i=1
    if c> m:
        t=True
        while t and i<=m:
            if (c-i)%(m+1)==0:
                t=False
                r=i
            i+=1
        if t:
            r=m
    else:
        r=c
    return r

def usuario_escolhe_jogada (c,m):
    r=0
    i=1
    while i==1:
        r=int(input("\nQuantas peças você vai tirar? "))
        if r>0:
            if r<=m and r<=c:
                i=0
            else:
                print("Resposta invalida ! ")
                i=1
    return r

def campeonato ():
        print("\nVocê escolheu um campeonato!")
        i=1
        j=0
        while i<=3:
            print("\n**** Rodada",i,"****")
            i+=1
            j=partida()
        c=3-j
        print("\n**** Final do campeonato! ****")
        print("\nPlacar: Você",c,"X",j,"Computador")

def main():
    i=1
    while i==1:
        r=int(input(("Bem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato \n:")))
        if r==1 or r==2:
            if r==1:
                i=0
                print("\nVocê selecionou a opção partida isolada!")
                partida()
            else:
                i=0
                campeonato()
        else:
            print("\nResposta invalida !\n")
            i=1
        
main()
