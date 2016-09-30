# -*- coding: utf-8 -*-

from expects import *

from fizzbuzz import fizzbuzz


with describe('The Fizzbuzz game'):
    with context('when the given number is 3'):
        with it('returns "Fizz"'):
            expect(fizzbuzz(3)).to(equal('Fizz'))

    with context('when the given number is divisible by 3'):
        with it('returns "Fizz"'):
            expect(fizzbuzz(9)).to(equal('Fizz'))

    with context('when the given number is 5'):
        with it('returns "Buzz"'):
            expect(fizzbuzz(5)).to(equal('Buzz'))

    with context('when the given number is divisible by 5'):
        with it('returns "Buzz"'):
            expect(fizzbuzz(10)).to(equal('Buzz'))



# Devuelve Buzz si el número es divisible por 5.
# Devuelve FizzBuzz si el número es divisible por 3 y por 5.
