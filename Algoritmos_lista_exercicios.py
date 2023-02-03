#EXECERICIO 1)
#print("Hello word")

#EXERCICIO 2)
#first_name = input("What is your name? :")
#last_name = input("What is your last name?: ")
#print("ola " + first_name +" "+ last_name + ", é um prazer te conhecer")
#
#EXERCICIO 3)
#nome = input("Nome do Funcionario: ")
#sal = (input("Salario: "))
#print ("O funcionário " + nome + " tem um salário de "+ sal + " em junho.")
#
#EXERCICIO 4)
#b = int(input("apresenteo segundo valor: "))
#answer = a + b
#print("A soma entre " + str(a) + " e " + str(b) + " é igual a " + str(answer))
#
#EXERCICIO 5)
#a = float(input("input the fist number: "))
#b = float(input("Input the second number: "))
#answer = (a + b)  / 2
#print("The average between " + str(a) +" e " + str(b) + " it´s the same as " + str(answer))
#
#EXERCICIO 6)
#x = int(input("input the number: "))
#before = x - 1
#after = x + 1
#print("The predecessor of " + str(x) +" is " + str(before))
#print("The sucessor of " + str(x) + " is " + str(after))
#
#EXERCISE 7)
#x = float(input("input the number: "))
#y = x * 2
#z = x / 3
#print("the double of " + str(x) + " is " + str(y))
#print("the third par of " + str(x) + " is " + str(z))
#
#exercise 8)
#x = float(input("input the distance in meters: "))
#print("the distance of "+ str(x) + " m " + "stands for")
#a = x *0.001
#b = x * 0.01
#c = x * 0.1
#d = x * 10
#e = x * 100
#f = x * 1000
#print(str(a) + " km ")
#print(str(b) + " Hm")
#print(str(c) + " Dam")
#print(str(d) + " dm")
#print(str(e) + " cm")
#print(str(f) + " mm")
#
#EXERCISE 9)
#reais = float((input("How much R$ do you have?: ")))
#dollars = reais / 3.45
#dollars = float("%0.2f" % (dollars))
#print("Your R$ " + str(reais)  + " are in " + " $ " + str(dollars))
# 
#EXERCISE 10)
#h = float(input("input with height: "))
#l = float(input("input with leght :"))
#are = h * l
#lt = are / 2
#print("The total area is "+ str(are) + " m2" + " and the amount of paint needed is " + str(lt) + " liter")
#
#EXERCICE 11)
#import math
#a = int(input("a = "))
#b = int(input("b = "))
#c = int(input("c = "))
#delta = b ** 2 - (4 * a * c)
#
#if delta < 0:
#    print("DELTA = " + str(delta))
#    print("The is no real roots")
#elif delta == 0:
#    x1 = -b / (2 * a)
#    print("DELTA =" + str(delta))
#    print("x1 = x2 = " + str(x1))
#else:
#    x1 = (-b - math.sqrt(delta)) / (2 * a)
#    x2 = (-b + math.sqrt(delta)) / (2 * a)
#    print("x1 = " + str(round(x1)))
#    print("x2 = " + str(round(x2)))

#EXERCICE 12)

#a = float(input("input the price tag: "))
#b = a -(a * 5) / 100
#print("The price is " + str(float("%0.2f" % (b))))

#EXERCISE 13)
#a = float(input("digite o salario: "))
#b = a + (a * 15) / 100
#print("Seu novo salario: " + str(float("%0.2f" % (b))))

#EXERCISE 14)
#a = int(input("km rodado: "))
#b = int(input("dia usados: "))
#c = 90 * b + 0.2 * a
#print("valor a pagar: R$" + str(float("%0.2f" % (c))))

#exercice 15)
#a = int(input("dias trabalhados: "))
#b = a * 8 * 25
#print("com " + str(a) + " dias trabalhados, valor ganho: " + str(float("%0.1f" % (b))))

#EXERCISE 16)
#print("Calculo de tempo de vida Perdido para fumantes")
#ciga = int(input("Cigarros fumados por dia: "))
#ano_periodo = int(input("Anos como fumante: "))
#min_anual = (ciga *10) * (365 * ano_periodo)
#print("ano_peiodo = " + str(ano_periodo))
#print("min_anual = " + str(min_anual))
#print("tempo de vida perdido em min por ano: ")
#dia_v_perdido = min_anual / 1440
#print(str(float("%0.0f" % (dia_v_perdido))))

#EXERCISE 17)
#print("Verificador de Multas")
#v_afer = int(input("Velocidade: "))
#if v_afer <= 80:
#    print("Veiculo Liberado")
#else:
#    print("Veiculo Multado")
#    v_mult = v_afer - 80
#    pag_mult = v_mult * 5
#    print("Sua multa R$ " + str(pag_mult))

#EXERCISE 18)
#print("Verificador Eleitoral")
#ano_nasc = int(input("Digite o ano de Nascimento (yyyy): "))
#ano_atual = int(input("Digite o ano atual (yyyy): "))
#idade = ano_atual - ano_nasc
#if idade <= 17:
#    print("Por se menor de idade e ter " + str(idade) + " anos, você não pode votar")
#else:
#    print("Parabens, por ser maior de idade e ter " + str(idade) + " você já pode votar")

#EXERCISE 19)
#print("Resultado Notas")
#nome = input("NOME DO ALUNO: ")
#n1 = int(input("NOTA 01: "))
#n2 = int(input("NOTA n2: "))
#med = (n1 + n2) / 2
#print("MÉDIA: " + str(med))
#if med >= 7:
#    print(nome + " sua média é "+ str(med) + " Paravens pelo bom aproveitamento")
#else:
#    print(nome + " sua média é " + str(med) + " meus pesames pelo mal aproveitamento")

#EXERCISE 20)
#print("Digite um numero e decubra PAR/IMPAR")
#n1 = int(input("Digite seu número: "))
#r = n1 - 2 * (n1 // 2) #r = n1 % 2
#if n1 - 2 * (n1 // 2) == 0:
#    print("seu número é PAR")
#else:
#    print("Seu número é IMPAR")

#EXERCISE 21)
#ano = int(input("Digite um ano (yyyy e descubra se é bixesto: "))
#if ano - 4  * (ano // 4) == 0:
#    print(str(ano) + " é bixesto")
#else:
#    print(str(ano) + " não é bixesto")

#EXERCISE 22)
#print("Alistamento militar")
#ano_nasc = int(input("Informe seu ano de nascimento(yyyy): " ))
#idade = 2023 - ano_nasc
#if idade <= 18:
#    idade_menor = 18 - idade
#    print("falta " + str(idade_menor) + " anos para vocé se alistar")
#else:
#    idade_maior = idade - 18
#    print("Vocé esta " + str(idade_maior) + " anos atrasado no alistamento")

#EXERCISE 23)
#print("Mega Promoção")
#print("Preencha seus dados e veja quanto ganha em desconto")
#nome = input("NOME: ")
#g = input("GENERO (M\F): ")
#valor_comp = float(input("Valor de suas compras: "))
#if g == "M" or g == "m":
#   valor_prom = valor_comp - ((valor_comp  * 5) / 100)
#    print("Parabens você tem 5% de deconto em suas compra R$ " + str(valor_prom ))
#else:
#    valor_prom = valor_comp - ((valor_comp * 13) / 100)
#    print("Parabens voce tem 13% de desconto em suas compras R$ " + str(valor_prom))    

#EXERCISE 24)
#print ("Tabajara Turismo")
#km = int(input("Percurso desejado em km: "))
#if km <= 200:
#   km_cobr = km * 0.5
#    print("Seu percurso de km " + str(km) + " tem um csto de R$ " + str(float("%0.2f" % (km_cobr))))
#elif km > 201:
#    km_cobr = km * 0.45
#    print("Seu percurso de km" + str(km) + " tem um custo de R$ "+ str(float("%0.2f" % (km_cobr))))

#EXERCISE 25)
#print("Faz triangulo?")
#n1 = int(input("RETA 01: "))
#n2 = int(input("RETA 02: "))
#n3 = int(input("RETA 03: "))
#if (n1 < (n2 + n3)) and (n2 < (n1 + n3)) and (n3 < (n2 + n1)):
#    print("É possivel foram triangulo")
#else:
#    print("Não é povivel formar truiangulo")

#EXERCISE 26)
#print("Digite os valores para comparação")
#v1 = int(input("VALOR 01: "))
#v2 = int(input("VALOR 02: "))
#if v1 > v2:
#    print("O primeiro valor é maior")
#elif v2 > v1:
#    print("O segundo valor é maior")
#else:
#    v1 == v2
#    print("Não existe maior, os dois são iguais")

#EXERCISE 27)
#print("Média e STATUS do Semestre")
#n1 = float(input("NOTA 01: "))
#n2 = float(input("NOTA 02: "))
#med = (n1 + n2) / 2
#if med <= 4.9:
#    print("reprovado")
#elif med >= 5 and med <= 6.9:
#    print(" em recuperação")
#elif med >= 7.0:
#    print("aprovado")

#EXERCISE 28)
#print("Classificação Territorial")
#print("-------------------------")

#l = int(input("Informe a Largura do Terreno:"))
#c = int(input("informe o comptimento do terreno"))
#h = l * c
#if h <= 100:
#    print("O terreno possui " + str(h) + " m2. Classificação: Terreno Popupar") 
#    print("---------------------")
#if h >= 100 and h <= 500:
#    print("O terreno possui " + str(h) + " m2. Classificação: Terreno master")
#    print("---------------------")
#if h >= 501:
#    print("O terreno possui " + str(h) + " m2. Calassificação: Terreno de VIP")


#EXERCISE 29)
#print("-------------------------")
#print("TABELA DE PROMOÇOES DO RH")
#print("-------------------------")
#nome = input("NOME DO FUNCIONARIO: ")
#sal = float(input("SALÁRIO DO FUNCIONARIO: "))
#anos = int(input("ANOS TRABALHADOS: "))
#if anos <= 3:
#    nsal = sal + (sal * 3) / 100
#    print(nome + " recebe o almento de 3% passando a receber R$ "+ str(nsal))
#elif anos > 3 and anos <= 10:
#    nsal = sal + (sal * 12.5) / 100
#    print(nome + " recebe o almento de 12.5% passando a receber R$ " + str(nsal))
#elif anos > 10 and anos <= 20:
#    nsal = sal + (sal * 20) / 100
#    print(nome + " recebe o almento de 20% passando a receber R$ " + str(nsal))
 
#EXERCISE 30)
#resp = "sim"
#equi = iso = tri = esc = bool
#while resp == "sim":
    #print("------------------------------------------")
    #print("Verifique a exixtencia e tipo de triangulo")
    #print("Forneça os lados do triângulo")
    #l1 = int(input("l1 = "))
    #l2 = int(input("l2 = "))
    #l3 = int(input("l3 = "))
    #tri = (l1 <l2 + l3) and (l2 < l1 + l3) and (l3 <l1 + l2)
    #print("FORMA TRIANDULO: " + str(tri))
    #equi = (l1 == l2) and (l1 == l3) and tri
    #print("FORMA EQUILATERO: " + str(equi)) 
    #iso = (l1==l2) and (l1!=l3) and tri or (l2==l3) and (l1!=l2) and tri or (l3==l1) and (l3!=l2) and tri
    #print("FORMA ISOCELES: " + str(iso))
    #esc = (l1!=l2) and (l1!=l3) and (l2!=l3) and tri
    #print("FORMA ESCALENO: " + str(esc))
    #print("-----------------------------------------")
    #resp = input("Deseja continuar [sim/não]:  ")

#EXERCISE 31)
#resp = "sim"
#while resp == "sim":
    
    #print("Partidas de JoKenpo")
    #print("[[1]PEDRA")
    #print("[2]PAPEL")
    #print("[3]TESOURA")
    #n1 = int(input("ESCOLHA: "))
    #n2 = int(input("ESCOLHA: "))
    #if (n1 == 1) and (n2 == 2) or (n2 == 1 ) and (n1 ==2):
    #    print("PAPEL GANHA DE PEDRA")
    #elif (n1 == 1) and (n2 == 3) or (n1 == 3) and (n2 == 1):
    #    print("PEDRA GANHA DE TESOURA")
    #elif (n1 == 2) and (n2 == 3) or (n1 == 3) and (n2 == 2):
    #    print("TESOURA GANHA DE PAPEL")
    #resp = input("Deseja continuar [sim/não]: ")
    #print("---------------------------------------")
    #print("---------------------------------------")

#EXERCISE 33)
#resp = "sim"
#while resp == "sim":
#    print("CASA DE EMPRESTIMO")
#    n1 = float(input("VALOR DO IMOVEL: "))
#    n2 = float(input("SALÁRIO: "))
#    n3 = int(input("PRAZO PAGAMENTO [anos]: "))
#    n4 = n2*0.3
#    n5 = n3*12
#    n6 =n1/n5
#    if n6 < n4:
#        print("Esprestimo altorizado de " + str(n5) + " meses e no valor de R$ " + str(float("%0.2f" % n6)))
#    else:
#        print("Emprestimo negado devido valor da parcelas R$ " + str(float("%0.2f" % n6)) + " esta acima de 30% do seu salário R$ " + str(float("%0.2f" % n4)))
#    resp = input("Deseja continuar [sim/não]: ")
#    print("-------------------------------")
#    print("-------------------------------")
#
#exercise 34)

#resp = "sim"
#while resp == "sim":
#    print("---------TABELA DE IMC---------")
#    print("Abaixo de 18.5: Abaixo do peso")
#    print("Entre 18.5 e 24: Peso ideal")
#    print("Entre 25 e 30: Sobrepeso")
#    print("Entre 30 e 40: Obesidade")
#    print("Acima de 40: Obesidade Mórbida")
#    print("-------------------------------")
#    n1 = int(input("Fornceça seu Peso: "))
#    n2 = float(input("Forneça sua altura: "))
#    imc = (n1 / (n2**2))
#    if imc  <= 18.5:
#        print("IMC de " + str(float("%0.2f" % imc)) + " : ABAIXO DO PESO")
#    elif imc > 18.5 and imc <= 25:
#        print("IMC de " + str(float("%0.2f" % imc)) + ": PESO IDEAL")
#    elif imc > 25 and imc <= 30:
#        print("IMC de " + str(float("%0.2f" % imc)) + ":OBESIDADE")
#    elif imc > 30 and imc < 40:
#        print("IMC de " + str(float("%0.2f" % imc)) + ":OBESIDADE MORBIDA")
#    resp = input("Deseja proceguir [sim/não]: ")
#    print("----------------------------------")
#    print("----------------------------------")
#
#EXERCISE 35)
#resp = "sim"
#def x():
#    print("Veiculo invalido")
#while resp == "sim":
#    print("LOCATIVA VEICULOS")
#    print("[1] CARRO POPULAR")
#    print("[2] CARROS DE LUXO")
#   
#    
#    choise = int(input("Escolha o carros: "))
#    if choise > 2:
#        x()
#    else:
#        n1 = int(input("Km do veiculo: "))
#        n2 = int(input("Dias de aluguel: "))
#        n3 = float()
#        match choise:
#            case 1:
#                if n1 <= 100:
#                    n3 = 90 * int(n2) + int(n1) * 0.2
#                    print("O veiculo popular foi alugado por " + str(n2) + " dias. Valor a pagar R$ " + str(float("%0.2f" % n3)))
#                else:
#                    n3 = 100 * int(n2) + int(n1) * 0.1
#                    print("O veiculo de luxo foi alugado por" + str(n2) + " dias. Valor a pagar R$ " + str(float("%0.2f" % n3)))
#            case 2:
#                if n1 <= 200:
#                    n3 = 150 * int(n2) + int(n1) * 0.2
#                    print("O veiculo de luxo foi alugado por " + str(n2) + " dias. Valor a pagar R$ " + str(float("%0.2f" % n3)))
#                else:
#                    n3 = 150 * int(n2) + int(n1) * 0.25
#                    print("O veiculo de luxo foi alugado por " + str(n2) + " dias. Valor a pagar R$ " + str(float("%0.2f" % n3)))
#            case _:
#                print("Valor incorreto")    
#        resp = input("Deseja continuar [sim/não]: ")
#    print("------------------------------")
#    print("------------------------------")

