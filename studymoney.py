entrada = []
entradasoma = float(0)
saida = []
saidasoma = float(0)

print('============================')
print('======== StudyMoney ========')
print('============================')
objetivo = input('Insira para qual objetivo você quer guardar dinheiro: ')
valor = float(input('Insira o valor para alcançar seu objetivo: '))
print('Seu objetivo e meta foram cadastrados!')

while True:
    print('============================')
    print('1 - Registrar Entrada\n2 - Registrar Gastos\n3 - Status\n4 - Sair')
    selecionar = int(input('Escolha entre "1-2-3-4": '))
    print('============================')

    # === OPÇÃO 1: ENTRADAS ===
    if selecionar == 1:
        while selecionar == 1:
            entradadados = []
            entradanome = input('Insira o nome da entrada (Salário, bico, mesada): ')
            entradadados.append(entradanome)

            entradavalor = float(input('Insira o valor: '))
            entradasoma = entradasoma + entradavalor
            entradadados.append(entradavalor)
            entrada.append(entradadados)

            decisao = input('Deseje adicionar outra entrada "S ou N"? ').upper()
            if decisao == 'N':
                break
            elif decisao != 'S':
                print('Opção inválida! Voltando ao menu automaticamente.')
                break

    # === OPÇÃO 2: GASTOS ===
    elif selecionar == 2:
        while selecionar == 2:
            saidadados = []
            saidanome = input('Insira o nome do gasto (Lanche, viagens, compras): ')
            saidadados.append(saidanome)

            saidavalor = float(input('Insira o valor: '))
            saidasoma = saidasoma + saidavalor
            saidadados.append(saidavalor)
            saida.append(saidadados)
            
            decisao = input('Deseje adicionar outra entrada "S ou N"? ').upper()
            if decisao == 'N':
                break
            elif decisao != 'S':
                print('Opção inválida! Voltando ao menu automaticamente.')
                break



    elif selecionar == 3:
        faltante = valor - (entradasoma - saidasoma)
        print('\n============================')
        print('=== Status Atual da Meta ===')
        print('============================')
        print('Meta:',objetivo,'\nValor:',valor)
        print('============================')
        print('====== Entrada/Saída =======')
        print('============================')
        print('Entrada:',entradasoma,'\nSaída:',saidasoma)
        print('Total:',entradasoma - saidasoma,'\nFalta:',faltante)
        print('============================')
        print('====== Tabela Entrada ======')
        print('============================')
        for linha in entrada:
            print(f"Entrada: {linha[0]} | Valor: R$ {linha[1]}")
        print('============================')
        print('======= Tabela Saída =======')
        print('============================')
        for linha in saida:
            print(f"Saída: {linha[0]} | Valor: R$ {linha[1]}")
        print('============================')
        decisao = input('Deseje voltar "S ou N"? ').upper()
        if decisao == 'N':
            break
        elif decisao != 'S':
            print('Opção inválida! Voltando ao menu automaticamente.')
    
    elif selecionar == 4:
        print('Encerrando o StudyMoney. Até logo!')
        break
    else:
        print('Opção inválida no menu! Escolha de 1 a 4.')
