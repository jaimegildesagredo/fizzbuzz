# -*- coding: utf-8 -*-

from fizzbuzz import fizzbuzz


def main():
    for i in range(1, 101):
        print i, fizzbuzz(i)

if __name__ == '__main__':
    main()
