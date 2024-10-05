#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from task1 import Pair, make_pair


class TestPair(unittest.TestCase):
    def setUp(self):
        self.pair1 = Pair(2.5, 3)
        self.pair2 = Pair(1.5, 2)

    def test_initialization(self):
        self.assertEqual(self.pair1.first, 2.5)
        self.assertEqual(self.pair1.second, 3)
        self.assertRaises(ValueError, Pair, 'not_a_float', 3)
        self.assertRaises(ValueError, Pair, 2.5, 'not_an_int')

    def test_read(self):
        # Проверяем, что метод read() не вызывает ошибок и обновляет значения
        with unittest.mock.patch('builtins.input', side_effect=[2.7, 4]):
            self.pair1.read()
            self.assertEqual(self.pair1.first, 2.7)
            self.assertEqual(self.pair1.second, 4)

    def test_display(self):
        # Проверяем вывод на экран
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.pair1.display()
            mocked_print.assert_called_once_with("Первое число: 2.5, Второе число: 3")

    def test_power(self):
        self.assertEqual(self.pair1.power(), 2.5 ** 3)
        self.assertEqual(self.pair2.power(), 1.5 ** 2)

    def test_make_pair(self):
        valid_pair = make_pair(3.5, 2)
        self.assertIsNotNone(valid_pair)
        self.assertEqual(valid_pair.first, 3.5)
        self.assertEqual(valid_pair.second, 2)

        invalid_pair = make_pair('invalid', 3)
        self.assertIsNone(invalid_pair)


if __name__ == '__main__':
    unittest.main()
