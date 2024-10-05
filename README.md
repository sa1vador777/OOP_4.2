# Объектно-ориентированное программирование. Лабораторная работа №2 (4.2). Вариант - 2.

## [Ссылка на отчет](docs/lr3.pdf)

## Структура репозитория

```
├── docs
│   ├── lr3.docx  <-------------| Отчет docx |
│   └── lr3.pdf  <--------------| Отчет pdf |
├── examples  <-----------------| Примеры из ЛР |
│   └── ...
├── LICENSE
├── README.md
└── src  <----------------------| Индивидуальные задания |
    ├── task1.py
    ├── task2.py
    └── tests <-----------------| Тесты |
        ├── first_task_tests.py
        └── second_task_tests.py
```

## Задания, Вариант - 2

### [Индивидуальное задание №1](src/task1.py)

Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально задействовав
имеющиеся в Python средства перегрузки операторов.

### [Индивидуальное задание №2](src/task2.py)

Создать класс Decimal для работы с беззнаковыми целыми десятичными числами,
используя для представления числа список из 100 элементов типа int, каждый из которых
является десятичной цифрой. Младшая цифра имеет меньший индекс (единицы — в
нулевом элементе списка). Реальный размер списка задается как аргумент конструктора
инициализации. Реализовать арифметические операции, аналогичные встроенным для
целых и операции сравнения.

Дополнительно к требуемым в заданиях операциям перегрузить операцию индексирования [].
Максимально возможный размер списка задать константой. В отдельном поле size должно
храниться максимальное для данного объекта количество элементов списка; реализовать метод
size(), возвращающий установленную длину. Если количество элементов списка изменяется во
время работы, определить в классе поле count. Первоначальные значения size и count
устанавливаются конструктором. В тех задачах, где возможно, реализовать конструктор инициализации строкой.
