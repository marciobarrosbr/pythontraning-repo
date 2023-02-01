#EXECERICIO 1)
#print("Hello word")

#EXERCICIO 2)
#first_name = input("What is your name? :")
#last_name = input("What is your last name?: ")
#print("ola " + first_name +" "+ last_name + ", é um prazer te conhecer")

#EXERCICIO 3)
#nome = input("Nome do Funcionario: ")
#sal = (input("Salario: "))
#print ("O funcionário " + nome + " tem um salário de "+ sal + " em junho.")

#EXERCICIO 4)
#b = int(input("apresenteo segundo valor: "))
#answer = a + b
#print("A soma entre " + str(a) + " e " + str(b) + " é igual a " + str(answer))

#EXERCICIO 5)
#a = float(input("input the fist number: "))
#b = float(input("Input the second number: "))
#answer = (a + b)  / 2
#print("The average between " + str(a) +" e " + str(b) + " it´s the same as " + str(answer))

#EXERCICIO 6)
#x = int(input("input the number: "))
#before = x - 1
#after = x + 1
#print("The predecessor of " + str(x) +" is " + str(before))
#print("The sucessor of " + str(x) + " is " + str(after))
 
#EXERCISE 7)
#x = float(input("input the number: "))
#y = x * 2
#z = x / 3
#print("the double of " + str(x) + " is " + str(y))
#print("the third par of " + str(x) + " is " + str(z))

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

#EXERCISE 9)
#reais = float((input("How much R$ do you have?: ")))
#dollars = reais / 3.45
#dollars = float("%0.2f" % (dollars))
#print("Your R$ " + str(reais)  + " are in " + " $ " + str(dollars))
 
#EXERCISE 10)
#h = float(input("input with height: "))
#l = float(input("input with leght :"))
#are = h * l
#lt = are / 2
#print("The total area is "+ str(are) + " m2" + " and the amount of paint needed is " + str(lt) + " liter")

#EXERCICE 11)
#import math
#a = int(input("a = "))
#b = int(input("b = "))
#c = int(input("c = "))
#delta = b ** 2 - (4 * a * c)

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
print("Faz triangulo?")
n1 = int(input("RETA 01: "))
n2 = int(input("RETA 02: "))
n3 = int(input("RETA 03: "))
if (n1 < (n2 + n3)) and (n2 < (n1 + n3)) and (n3 < (n2 + n1)):
    print("É possivel foram triangulo")
else:
    print("Não é povivel formar truiangulo")
