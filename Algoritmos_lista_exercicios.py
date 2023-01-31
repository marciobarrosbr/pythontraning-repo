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