#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('P.fa') as f:
    p = f.read().strip()

with open('T.fa') as f:
    t = f.read().strip()


n = len(t)
s = [[0] * 2 for _ in range(n)] # генерируем двумерный массив из нулей

for i in range(n):
    s[i][0] = i # в первый столбец номера 0 1 2 3 и тд
    s[i][1] = t[i:] # во второй суффиксы

s.sort(key=lambda arr: arr[1]) # сортируем лексико-графически

array=[0]*n

for i in range(n):
    array[i] = s[i][0] # сделали одномерный массив индексов


def bisect_left(array, query, seq, lo=0, hi=None):
    if lo < 0:
        raise ValueError('must be non-negative')
    if hi is None: #по умолчанию правая граница это последний элемент
        hi = len(array)
    while lo < hi: 
        mid = (lo+hi)//2 #середина отрезка
        if seq[array[mid]:] < query: # двигаем левую либо правую границу
            lo = mid+1
        else:
            hi = mid

    def match_at(i):
        return seq[i: i + len(query)] == query

    if not match_at(array[lo]):
        raise IndexError('there is not any index for the query')

    # array[lo] это первое вхождение
    # теперь идем назад чтобы найти все
    first = lo
    while first > 0 and match_at(array[first - 1]):
        first -= 1

    # и двигаемся вправо чтобы найти последнее
    last = lo
    while match_at(array[last]):
        last += 1
    
    for i in range(len(array)):
        array[i] += 1 # делаем человеческую нумерацию с 1
         
    return array[first:last]

print(bisect_left(array, p, t))



