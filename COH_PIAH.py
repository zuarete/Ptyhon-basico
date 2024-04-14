import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    similariedade=0
    sim=0
    i=0
    while i<6:
        similariedade=abs(as_a[i]-as_b[i])+similariedade
        i=i+1
        
    similariedade=similariedade/6

    if similariedade>sim:
        sim=similariedade
    return sim


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #Tamanho médio de palavra
    lista_sentencas = separa_sentencas(texto)
    lista_frases = []
    for sentenca in lista_sentencas:
        lista_frases.extend(separa_frases(sentenca))

    lista_palavras = separa_palavras(" ".join(lista_frases))

    total_palavras = len(lista_palavras)

    tamanho_palavras = sum(len(palavra) for palavra in lista_palavras)

    tam_med_palavra=tamanho_palavras/total_palavras

    # Type-Token

    numero_de_palavras_diferentes=n_palavras_diferentes(lista_palavras)

    type_token=numero_de_palavras_diferentes/total_palavras

    #Hapax Legomana

    numero_de_palavras_unicas=n_palavras_unicas(lista_palavras)

    hapax_legomana=numero_de_palavras_unicas/total_palavras

    #Tamanho médio de sentença
    lista_sentencas=separa_sentencas(texto)
    total_sentecas=len(lista_sentencas)

    caracteres = sum(len(sentenca) for sentenca in lista_sentencas)

    tamanho_medio_sentenca=caracteres/total_sentecas

    #Complexidade de sentença 
    total_frases = len(lista_frases)

    complexidade_sentenca=total_frases/total_sentecas

    #Tamanho médio de frase
    total_frases = len(lista_frases)

    caracteres_frases = sum(len(frase) for frase in lista_frases)

    tamanho_medio_frase=caracteres_frases/total_frases

    as_b=[tam_med_palavra, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]

    return as_b

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    ass_a=ass_cp
    lista_assinaturas=[]
    quantidade_textos=len(textos)
    i=1
    texto_provavel=1
    ass_b=calcula_assinatura(textos[0])
    similariedade=compara_assinatura(ass_a,ass_b)
    while i<quantidade_textos:
        ass_b=calcula_assinatura(textos[i])
        sim=compara_assinatura(ass_a,ass_b)
        if sim<similariedade:
            similariedade=sim
            texto_provavel=i+1
        i=i+1
    return texto_provavel

    pass

def main():
    ass_cp=le_assinatura()
    textos=le_textos()
    r=avalia_textos(textos,ass_cp)
    print("O autor do texto",r,"está infectado com COH-PIAH")


main()
