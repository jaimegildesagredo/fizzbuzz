# -*- coding: utf-8 -*-

from expects import *

from fizzbuzz import fizzbuzz


with describe('The Fizzbuzz game'):
    with context('when the given number is 3'):
        with it('returns "Fizz"'):
            expect(fizzbuzz(3)).to(equal('Fizz'))



# Devuelve Fizz si el número es divisible por 3.
# Devuelve Buzz si el número es divisible por 5.
# Devuelve FizzBuzz si el número es divisible por 3 y por 5.
