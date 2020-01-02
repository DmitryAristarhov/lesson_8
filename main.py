# -*- coding: utf-8 -*-
from functools import wraps
import time
import sys

# 1. Написать декоратор, замеряющий время выполнение декорируемой функции.
# 2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000
# (создание объектов оформить в виде функций).
# PRO
# Light +
# 3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
# 4. Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами:
# натуральные числа от 1 до 1000000.


def time_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.monotonic()
        res = func(*args, **kwargs)
        end = time.monotonic()
        print('time =', end - begin)
        return res
    return wrapper


def memory_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Будем считать что занимаемая память это размер самой функции плюс размер данных на входе и выходе.
        memory = sys.getsizeof(func)
        for i in args:
            memory += sys.getsizeof(i)
        for i in kwargs.values():
            memory += sys.getsizeof(i)
        res = func(*args, **kwargs)
        memory += sys.getsizeof(res)
        print('memory =', memory)
        return res
    return wrapper


@time_func
@memory_func
def my_sleep_func(n):
    time.sleep(n)


@time_func
@memory_func
def create_list(n):
    return [i for i in range(1, n + 1)]


@time_func
@memory_func
def create_gen(n):
    return (i for i in range(1, n + 1))


@memory_func  # Для разнообразия, в другом порядке декораторы поставим)
@time_func
def use_sequence(sequence):
    s = 0
    for _ in sequence:
        s += 1
    return s


print('my_sleep_func(0.1)')
my_sleep_func(0.1)
print()

print('my_list = create_list(1000000)')
my_list = create_list(1000000)
print()

print('use_sequence(my_list)')
use_sequence(my_list)
print()

print('my_gen = create_gen(1000000)')
my_gen = create_gen(1000000)
print()

print('use_sequence(my_gen)')
use_sequence(my_gen)
print()

print('Время затрачиваемое на генерацию последовательности больше чем на создание генератора.')
print('Время затрачиваемое на работу с последовательностью немного меньше чем на работу с генератором.')
print('Сумарное время затрачиваемое на генерацию и работу, для последовательности сопоставимо, '
      'но все же немного меньше чем для генератора.')
print('Память необходимая для работы с последовательностью на порядки больше чем для работы с генератором.')
