import csv
a = {}
b = {}
c = {}
d = {}
i_n = []
comando = ''
print('=> restaurante aberto')
def _atmesas_():
    arq = input()
    with open(arq,newline='') as csvfile:
        reader = csvfile
        for row in reader:
            row = row.strip().split(', ')
            row[0] = int(row[0])
            if row[0] in a.keys():
                b[a[row[0]]['area']].remove(row[0])
            if row[1] not in b.keys():
                b[row[1]] = []
            b[row[1]].append(row[0])
            a[row[0]] = {'area': row[1], 'ocup': row[2]}
def _relmesa_():
    if b: 
        bb = sorted(b.items())
        for item in bb:
            print(f'area: {item[0]}')
            if not len(item[1]):
                print(f'- area sem mesas')
            else:
                for key in sorted(item[1]):
                    print(f'- mesa: {key}, status: {a[key]["ocup"]}')
    else:
        print(f'- restaurante sem mesas')
def _atcard_():
    arq = input()
    with open(arq,newline='') as csvfile:
        for row in csvfile:
            row = row.strip().split(', ')
            c[row[0]] = row[1:]
            if row[0] not in c.keys():
                c[row[0]].append(row[0])
            if row[0] == c.keys():
                c[row[0]] = row[1:]
def _relcard_():
    if c:
        ck = sorted(c.keys())
        cc = sorted(c.items())
        for keys in ck:
            print(f'item: {keys}')
            dic = {}
            for items in cc:
                if keys == items[0]:
                    for subitem in sorted(items[1]):
                        dic[subitem]=dic.get(subitem,0)+1
            print('\n'.join(f'- {item[0]}: {item[1]}' for item in dic.items()))    
    else:
        print(f'- cardapio vazio')           
def _atestoque_():
    arq = input()
    with open(arq,newline='') as csvfile:
        for row in csvfile:
            row = row.strip().split(', ')
            row[1] = int(row[1])
            if row[0] not in d.keys():
                d[row[0]] = row[1]
            else:
                d[row[0]] += row[1]
def _relestoq_():
    if d:
        fail = False
        dd = sorted(d.keys())
        for keys in dd:
            if d[keys] != 0:
                break
        else:
            print("- estoque vazio")
            fail = True
        if not fail:
            for keys in dd:
                if d[keys]:
                    print(f'{keys}: {d[keys]}')
    else:
        print('- estoque vazio')
def _fazerp_():
    n,i = map(str, input().split(', '))
    n = int(n)
    if n not in a:
        print(f'erro >> mesa {n} inexistente')
    elif a[n]['ocup'] == 'livre':
        print(f'erro >> mesa {n} desocupada')
    elif i not in c:
        print(f'erro >> item {i} nao existe no cardapio')
    else:
        dic = {}
        for item in c[i]:
            dic[item] = dic.get(item, 0) + 1
        for item in dic:
            try:
                if d[item] < dic[item]:
                    print(f"erro >> ingredientes insuficientes para produzir o item {i}")
                    break
            except:
                print(f"erro >> ingredientes insuficientes para produzir o item {i}")
                break
        else:
            for item in dic:
                d[item] -= dic[item]
            i_n.append((n,i))
            print(f"sucesso >> pedido realizado: item {i} para mesa {n}")
        

def _relpedidos_():
    if i_n:
        lista_sorted = sorted(i_n, key = lambda x : x[1])
        lista_sorted = sorted(lista_sorted)
        dic = {}
        for item in lista_sorted:
            if item[0] not in dic.keys():
                dic[item[0]] = []
                dic[item[0]].append(item[1])
            else:
                dic[item[0]].append(item[1])
        for chave in dic:
            print(f"mesa: {chave}")
            for item in dic[chave]:
                print(f"- {item}")

    else:
        print(f'- nenhum pedido foi realizado')
def _frestau_():
    if i_n:
        for i, item in enumerate(i_n):
            print(f"{i+1}. mesa {item[0]} pediu {item[1]}") 

    else:
        print(f'- historico vazio')
    
    print(f'=> restaurante fechado')
def _error_():
    print(f'erro >> comando inexistente')
while comando != '+ fechar restaurante':               
    comando = input()
    if comando == '+ atualizar mesas':
        _atmesas_()
    elif comando == '+ relatorio mesas':
        _relmesa_()
    elif comando == '+ atualizar cardapio':
        _atcard_()
    elif comando == '+ relatorio cardapio':
        _relcard_()
    elif comando == '+ atualizar estoque':
        _atestoque_()
    elif comando == '+ relatorio estoque':
        _relestoq_()
    elif comando == '+ fazer pedido':
        _fazerp_()
    elif comando == '+ relatorio pedidos':
        _relpedidos_()
    elif comando == '+ fechar restaurante':
        _frestau_()
    else:
        _error_()

