
chislo = int(input('Введите пятизначное целое число: '))
print ()

edinica = chislo%10
desiatok = chislo%100//10
sotnia = chislo//100%10
tysiacha = chislo//1000%10
desiatki_tysiach = chislo//10000
print ('Числа для операций получились:',edinica,desiatok,sotnia,tysiacha,desiatki_tysiach)
result = desiatok**edinica*sotnia/(desiatki_tysiach-tysiacha)
print ('Результат задания:', result)
