#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, first, second):
        if not isinstance(first, float):
            raise ValueError("Поле first должно быть дробным числом.")
        if not isinstance(second, int):
            raise ValueError("Поле second должно быть целым числом.")
        self.first = first
        self.second = second

    def read(self):
        try:
            self.first = float(input("Введите значение first (дробное число): "))
            self.second = int(input("Введите значение second (целое число): "))
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            return

    def display(self):
        print(f"Первое число: {self.first}, Второе число: {self.second}")

    def power(self):
        return self.first ** self.second

    # Перегрузка оператора сложения
    def __add__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first + other.first, self.second + other.second)
        raise ValueError("Операнд должен быть объектом Pair.")

    # Перегрузка оператора вычитания
    def __sub__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first - other.first, self.second - other.second)
        raise ValueError("Операнд должен быть объектом Pair.")

    # Перегрузка оператора сравнения (по полю first)
    def __eq__(self, other):
        if isinstance(other, Pair):
            return self.first == other.first and self.second == other.second
        return False

    def __lt__(self, other):
        if isinstance(other, Pair):
            return (self.first, self.second) < (other.first, other.second)
        return False

    # Приведение к строке для удобного вывода
    def __str__(self):
        return f"({self.first}, {self.second})"

def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка создания пары: {e}")
        return None

if __name__ == "__main__":
    # Демонстрация работы программы
    
    # Пример использования make_pair
    pair1 = make_pair(2.5, 3)
    pair2 = make_pair(1.5, 2)
    if pair1 and pair2:
        print(f"pair1: {pair1}")
        print(f"pair2: {pair2}")
        
        # Демонстрация перегрузки операторов
        print("\nРезультат сложения: ", pair1 + pair2)
        print("Результат вычитания: ", pair1 - pair2)
        print("Равно ли pair1 и pair2? ", pair1 == pair2)
        print("pair1 меньше pair2? ", pair1 < pair2)

    print("\nЧтение данных с клавиатуры:")
    pair3 = Pair(0.0, 0)  # Создаем объект с заглушками
    pair3.read()          # Ввод значений с клавиатуры
    pair3.display()       # Выводим значения
    print(f"Результат возведения first в степень second: {pair3.power()}")
