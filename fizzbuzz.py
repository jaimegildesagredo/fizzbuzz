# -*- coding: utf-8 -*-


def fizzbuzz(number):
    if _is_fizzbuzz(number):
        return 'FizzBuzz'

    if _is_fizz(number):
        return 'Fizz'

    if _is_buzz(number):
        return 'Buzz'

    return number


def _is_fizz(number):
    return number % 3 == 0 or '3' in str(number)


def _is_buzz(number):
    return number % 5 == 0 or '5' in str(number)


def _is_fizzbuzz(number):
    return _is_fizz(number) and _is_buzz(number)
