import copy
from operator import itemgetter
entrada = str
condparada = ('--ATENDIMENTO')
ma = ''
numero = 0
ordem = []
listadeamc = []
cadeiras = []
def titulo(entrada):
    entrada = input()
titulo(entrada)
while ma != '--ATENDIMENTO':
    try:
        listinhaamc = []
        a, m, c = input().split()
        ordem.append(a)
        listinhaamc.append(a)
        listinhaamc.append(int(m))
        listinhaamc.append(int(c))
        listadeamc.append(listinhaamc)
        cadeiras.append(int(c))
    except:
        ma = '--ATENDIMENTO'
cloneamc = copy.deepcopy(listadeamc)
xxxxsomaxxxx = []
numerol = []
outral = []
ocupadas = []
listadeamc = sorted(listadeamc,key = itemgetter(0,2))
cloneamc = sorted(cloneamc,key = itemgetter(0,2))
def rem(ordem):
    l = []
    for v in ordem:
        if v not in l:
            l.append(v)
    l.sort()
    return l
ordem = rem(ordem)


tmesas = []

while numero != -1:
    numero = int(input())
    numerol.append(numero)
    xp = []
    outralista=[]
    if numero == 1:
        frase = input().split()
        x = int(frase[4])
        xp.append(x)
        y = frase[-1]
        np = True
        tp = (2*x)+2
        for o in listadeamc:
            listinha = []
            if y == o[0]:
                if x <= o[2]:
                    #print(f'Um grupo de {x} pessoas ocupou uma mesa de {o[2]} lugares na area {y}.')
                    #xxxxsomaxxxx.append(x)
                    if o[1] > 0:
                        o[1]=o[1]-1
                        listinha.append(o[0])
                        listinha.append(tp)
                        listinha.append(o[2])
                        listinha.append(x)
                        outral.append(listinha.copy())
                        ocupadas.append(o)
                        np = False
                        xxxxsomaxxxx.append(x)
                        print(f'Um grupo de {x} pessoas ocupou uma mesa de {o[2]} lugares na area {y}.')
                        
                        break
                    #else:
                        #listadeamc.remove(o)
                        #np = False
                        #break
        if np:
            print(f'Nao foi possivel levar o grupo de clientes para uma mesa.')
    
    if numero == 2:
        for i in ordem:
            listasubtr = []
            tmesastmp = []
            tmesassub = []
            for j in cloneamc:
                if i == j[0]:
                    tmesastmp.append(j[1])
            tmesastmp = sum(tmesastmp)
            
            for x in listadeamc:
                if i == x[0]:
                    tmesassub.append(x[1])
            tmesassub = sum(tmesassub)
            print(f'{i}: ({tmesastmp-tmesassub} de {tmesastmp} mesas)')
    if numero == 3:
        for i in ordem:
            listasubtr = []
            tmesastmp = []
            soma = 0
            #tmesassub = []
            for j in cloneamc:
                if i == j[0]:
                    tmesastmp.append(j[1]*j[2])
            tmesastmp = sum(tmesastmp)
            for z in outral:
                if i == z[0]:
                    soma+=z[3]
                    
            #for x in listadeamc:
                #if i == x[0]:
                    #tmesassub.append(x[1]*x[2])
            #tmesassub = sum(tmesassub)
            print(f'{i}: ({soma} de {tmesastmp} pessoas)')
        
    if numero == 4:
        frase = input().split()
        num = int(frase[3])
        num2 = int(frase[6])
        y = (frase[-1])
        n = (frase[1])
        if 'adicionar' == n:
            for t in cloneamc:
                if y == t[0]:
                    if num2 == t[2]:
                        t[1] = num+t[1]
                        
                        break
            else:
                cloneamc.append([y, num, num2])
                cloneamc.sort(key=lambda x:x[2])
                cloneamc.sort(key=lambda x:x[0])
                
                
            for t in listadeamc:
                if y == t[0]:
                    if num2 == t[2]:
                        t[1] = num+t[1]
                        print(f'{num} mesas de {num2} cadeiras adicionadas com sucesso na area {y}.')
                        break
            else:
                listadeamc.append([y, num, num2])
                listadeamc.sort(key=lambda x:x[2])
                listadeamc.sort(key=lambda x:x[0])
                print(f'{num} mesas de {num2} cadeiras adicionadas com sucesso na area {y}.')
        else:
            for c in cloneamc:
                if y == c[0]:
                    if num2 == c[2]:
                        c[1] = c[1]-num
                        #print(f'{num} mesas de {num2} cadeiras removidas com sucesso na area {y}.')
                        break
            for i in listadeamc:
                if y == i[0]:
                    if num2 == i[2]:
                        i[1] = i[1]-num
                        print(f'{num} mesas de {num2} cadeiras removidas com sucesso na area {y}.')
                        break
    if numero == -1:
        print(f'Restaurante fechado.')
        print(f'Balanco final de mesas:')
        
        ultarea = ''
        for i in cloneamc:
            if ultarea != i[0]:
                ultarea = i[0]
                print(f'{ultarea}:')
            print(f' {i[1]} mesas de {i[2]} cadeiras.')
        
        
        
        
        '''def rem(cadeiras):
            l2 = []
            for j in cadeiras:
                if j not in l2:
                    l2.append(j)
            l2.sort()
            return l2
        cadeiras = rem(cadeiras)
        cloneamc =  sorted(cloneamc, key = itemgetter(0,2))
        for v in ordem:
            print(f'{v}:')
            for k in cloneamc:
                if v == k[0]:
                    for c in cadeiras:
                        if c == k[2]:
                            print(f' {k[1]} mesas de {k[2]} cadeiras.')'''       
        try:
            print(f'Um total de {sum(xxxxsomaxxxx)} pessoas visitaram o restaurante hoje.')
            print(f'Bom descanso!')
        except:
            print(f'Um total de 0 pessoas visitaram o restaurante hoje.')
            print(f'Bom descanso!')   
        
    i = 0
    while i < len(outral):
        outral[i][1]-=1
        if not outral[i][1]:
            for j in range(len(listadeamc)):
                if listadeamc[j][0] == outral[i][0] and listadeamc[j][2]==outral[i][2]:
                    listadeamc[j][1]+=1
                    outral.pop(i)
                    i-=1
                    break
        i+=1
  
        