from natural import *
from integer import *
def INT_Q_B(Q):
    numerator = Q[0]
    denominator = Q[1]
    return not MOD_NN_N([numerator[1], numerator[2]], denominator)
# Гурьянов Савелий
# Функция возвращает отрицание результата остатка от деления числителя, преобразованного к натуральному числу,
# на натуральный знаменатель, если остаток равен нулю, то дробь преобразуется к натуральному числу, иначе не преобразуется и вернётся 0


def RED_Q_Q(Q):
    Q[0] = DIV_ZZ_Z(Q[0], [0] + GCF_NN_N(ABS_Z_N(Q[0]), Q[1]))
    Q[1] = DIV_ZZ_Z([0] + Q[1], [0] + GCF_NN_N(ABS_Z_N(Q[0]), Q[1]))[1:]
    return [Q[0], Q[1]]
# Гурьянов Савелий
# Числитель и знаменатель делятся на НОД знаменателя и числителя(числитель преобразуется к натуральному числу при помощи
# функции ABS_Z_N)

def ADD_QQ_Q(ch1, zn1, ch2, zn2):
# Пекло Елизавета
# Сложение дробей

# НОК и есть новый знаменатель дробей
    nok = LCM_NN_N(zn1, zn2)
# Находим множители при числителях дробей
    mn1 = DIV_ZZ_Z(nok, zn1)
    mn2 = DIV_ZZ_Z(nok, zn2)
# Находим сами числители, а затем и их сумму
    ch1 = MUL_ZZ_Z(ch1, mn1)
    ch2 = MUL_ZZ_Z(ch2, mn2)
    newCh = ADD_ZZ_Z(ch1, ch2)
# Возвращаем новые числитель и знаменатель
    return newCh, nok


def TRANS_Z_Q(x):
    # Артамонов Артур, гр.0306
    # Преобразование целого в дробное

    x.append("/")
    x.append(1)

    return x


def TRANS_Q_Z(x):
    # Артамонов Артур, гр.0306
    # Преобразование дробного в целое, если знам. = 1

    if x[-1] == 1:
        if x[-2] == '/':
            x = x[:-2]
    return x

def SUB_QQ_Q(list1,list2):
    #Дашкин Дамир
    #Вычитание дробей
    beginning_znam1 = list1.index('/')
    k1 = list1[beginning_znam1:]
    beginning_znam2 = list1.index('/')
    k2 = list2[beginning_znam2:]
    znam=LCM_NN_N(k1,k2)
    add1 = DIV_NN_N(znam, k1)
    add2 = DIV_NN_N(znam, k2)
    chisl1 = MUL_ZZ_Z(add1, list1[:beginning_znam1-1])
    chisl2 = MUL_ZZ_Z(add2, list2[:beginning_znam2-1])
    result = SUB_ZZ_Z(chisl1, chisl2)
    res = []
    res = result[1:] + ['/'] + znam
    return res