def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
    trocas = 0 #variavel aux
    #verifica qual das duas pessoas tem o menor/maior numero de fig
    menor_qtd_figurinha = figurinhas_da_maria if len(figurinhas_da_maria) <= len(figurinhas_do_joao) else figurinhas_do_joao
    maior_qtd_figurinha = figurinhas_da_maria if len(figurinhas_da_maria) >= len(figurinhas_do_joao) else figurinhas_do_joao
   
    for index, numero_figurinha in enumerate(menor_qtd_figurinha):
        if not numero_figurinha in maior_qtd_figurinha:
            for n in range(index, len(maior_qtd_figurinha)):
                if numero_figurinha != maior_qtd_figurinha[n]:
                    aux = maior_qtd_figurinha[n]
                    maior_qtd_figurinha[n] = numero_figurinha
                    menor_qtd_figurinha[index] = aux
                    trocas = trocas + 1
                    break
    return trocas



if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao)

