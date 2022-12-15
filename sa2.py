#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('P.fa') as f:
    p = f.read().strip()

with open('T.fa') as f:
    t = f.read().strip()


n = len(t)
s = [[0] * 2 for _ in range(n)] # генерируем двумерный массив из нулей

for i in range(n):
    s[i][0] = i # в первый вносим столбец номера 0 1 2 3 и тд
    s[i][1] = t[i:] # во второй вносим суффиксы

s.sort(key=lambda arr: arr[1]) # сортируем лексико-графически

array=[0]*n

for i in range(n):
    array[i] = s[i][0] # сделали одномерный массив индексов


def bisect_left(array, p, t, left=0, right=None):
    if left < 0:
        raise ValueError('должен быть неотрицательным')
    if right is None: # по умолчанию правая граница это последний элемент
        right = len(array)
    while left < right: 
        mid = (left+right)//2 # середина отрезка
        if t[array[mid]:] < p: # двигаем правую либо левую границу
            left = mid+1
        else:
            right = mid

    def match_at(i): # проверяет совпадения на i-месте
        return t[i: i + len(p)] == p

    if not match_at(array[left]):
        raise IndexError('индексы закончились')

    # array[left] это первое вхождение
    # теперь идем назад чтобы найти все вхождения
    first = left
    while first > 0 and match_at(array[first - 1]):
        first -= 1

    # и двигаемся вправо чтобы найти последнее
    last = left
    while match_at(array[last]):
        last += 1
    
    for i in range(len(array)):
        array[i] += 1 # делаем человеческую нумерацию с 1
         
    return array[first:last]

print(bisect_left(array, p, t))



