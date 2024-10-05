#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Decimal:
    MAX_SIZE = 100

    def __init__(self, size):
        """Инициализация списка с цифрами числа. Размер не может превышать MAX_SIZE."""
        if size > self.MAX_SIZE or size <= 0:
            raise ValueError(f"Размер числа должен быть в пределах от 1 до {self.MAX_SIZE}.")
        self.digits = [0] * size
        self.size = size
        self.count = 0

    def __repr__(self):
        """Строковое представление числа (старшие разряды идут первыми)."""
        return ''.join(map(str, reversed(self.digits)))

    def set_number(self, number):
        """Устанавливает число в виде списка цифр."""
        number_str = str(number)[::-1]
        if len(number_str) > self.size:
            raise ValueError(f"Число слишком большое для заданного размера: {self.size}")
        self.digits = [int(digit) for digit in number_str] + [0] * (self.size - len(number_str))
        self.count = len(number_str)

    def get_number(self):
        """Возвращает число как строку (старшие разряды идут первыми)."""
        return ''.join(map(str, reversed(self.digits))).lstrip('0') or '0'

    # Перегрузка оператора сложения
    def __add__(self, other):
        if isinstance(other, Decimal):
            result = Decimal(self.size)
            carry = 0
            for i in range(self.size):
                sum_digits = self.digits[i] + other.digits[i] + carry
                result.digits[i] = sum_digits % 10
                carry = sum_digits // 10
            result.count = max(self.count, other.count)
            return result
        raise ValueError("Числа должны быть одинакового размера и типа Decimal.")

    # Перегрузка оператора вычитания
    def __sub__(self, other):
        if isinstance(other, Decimal):
            result = Decimal(self.size)
            borrow = 0
            for i in range(self.size):
                diff_digits = self.digits[i] - other.digits[i] - borrow
                if diff_digits < 0:
                    diff_digits += 10
                    borrow = 1
                else:
                    borrow = 0
                result.digits[i] = diff_digits
            result.count = max(self.count, other.count)
            return result
        raise ValueError("Числа должны быть одинакового размера и типа Decimal.")

    # Перегрузка оператора умножения
    def __mul__(self, other):
        if isinstance(other, Decimal):
            result = Decimal(self.size)
            temp_result = [0] * (2 * self.size)
            for i in range(self.size):
                carry = 0
                for j in range(self.size):
                    mul_digits = self.digits[i] * other.digits[j] + temp_result[i + j] + carry
                    temp_result[i + j] = mul_digits % 10
                    carry = mul_digits // 10
            # Обрезаем лишние разряды
            result.digits = temp_result[:self.size]
            result.count = self.count + other.count
            return result
        raise ValueError("Числа должны быть одинакового размера и типа Decimal.")

    # Операция сравнения: ==
    def __eq__(self, other):
        if isinstance(other, Decimal):
            return self.digits == other.digits
        return False

    # Операция сравнения: <
    def __lt__(self, other):
        if isinstance(other, Decimal):
            return self.get_number() < other.get_number()
        return False

    # Операция сравнения: >
    def __gt__(self, other):
        if isinstance(other, Decimal):
            return self.get_number() > other.get_number()
        return False

    # Приведение к строке для удобного отображения
    def __str__(self):
        return self.get_number()

if __name__ == "__main__":
    # Демонстрация работы класса Decimal

    # Создаем два числа
    dec1 = Decimal(10)
    dec2 = Decimal(10)

    # Устанавливаем значения
    dec1.set_number(12345)
    dec2.set_number(6789)

    # Вывод чисел
    print("dec1:", dec1)
    print("dec2:", dec2)

    # Демонстрация операций
    print("\nРезультат сложения:", dec1 + dec2)
    print("Результат вычитания:", dec1 - dec2)
    print("Результат умножения:", dec1 * dec2)

    # Сравнение
    print("\ndec1 == dec2:", dec1 == dec2)
    print("dec1 > dec2:", dec1 > dec2)
    print("dec1 < dec2:", dec1 < dec2)

    # Проверка значений size и count
    print(f"\nРазмер dec1 (size): {dec1.size}")
    print(f"Количество активных цифр в dec1 (count): {dec1.count}")
