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

    with context('when the given number is divisible by 3 and 5'):
        with it('returns "FizzBuzz"'):
            expect(fizzbuzz(15)).to(equal('FizzBuzz'))

    with context('when the given number is not divisible by 3 nor 5'):
        with it('returns the same number'):
            expect(fizzbuzz(2)).to(equal(2))

    with context('when the given number is not divisible by 3 but contains a 3'):
        with it('returns "Fizz"'):
            expect(fizzbuzz(23)).to(equal('Fizz'))

    with context('when the given number is not divisible by 5 but contains a 5'):
        with it('returns "Fizz"'):
            expect(fizzbuzz(52)).to(equal('Buzz'))
