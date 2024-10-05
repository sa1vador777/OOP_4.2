#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from task2 import Decimal


class TestDecimal(unittest.TestCase):
    def setUp(self):
        self.dec1 = Decimal(5)
        self.dec2 = Decimal(4)
        self.dec1.set_number(12345)
        self.dec2.set_number(6789)

    def test_initialization(self):
        self.assertRaises(ValueError, Decimal, 0)
        self.assertRaises(ValueError, Decimal, 101)

    def test_set_number(self):
        self.dec1.set_number(1234)
        self.assertEqual(self.dec1.get_number(), '1234')
        self.assertRaises(ValueError, self.dec1.set_number, 12345678901234567890)  # Слишком большое число

    def test_addition(self):
        result = self.dec1 + self.dec2
        self.assertEqual(result.get_number(), '19134')

        dec3 = Decimal(6)
        dec3.set_number(99999)
        result = self.dec1 + dec3
        self.assertEqual(result.get_number(), '112344')

    def test_subtraction(self):
        result = self.dec1 - self.dec2
        self.assertEqual(result.get_number(), '5556')

        dec4 = Decimal(5)
        dec4.set_number(10000)
        result = self.dec4 - self.dec1
        self.assertEqual(result.get_number(), '8765')

    def test_multiplication(self):
        result = self.dec1 * self.dec2
        self.assertEqual(result.get_number(), '83865')

        dec5 = Decimal(6)
        dec5.set_number(10000)
        result = self.dec5 * self.dec1
        self.assertEqual(result.get_number(), '123450000')

    def test_equality(self):
        dec6 = Decimal(5)
        dec6.set_number(12345)
        self.assertTrue(self.dec1 == dec6)
        self.assertFalse(self.dec1 == self.dec2)

    def test_comparisons(self):
        self.assertTrue(self.dec1 > self.dec2)
        self.assertTrue(self.dec2 < self.dec1)
        self.assertFalse(self.dec1 < self.dec1)

if __name__ == '__main__':
    unittest.main()
