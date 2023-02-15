module Codewars.Kata.Fib where


fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

helper n (x:y:rest) = if x*y < n
                         then helper n (y:rest)
                         else (x,y,x*y == n)
                              

-- | Returns a pair of consecutive Fibonacci numbers a b,
--   where (a*b) is equal to the input, or proofs that the
--   number isn't a product of two consecutive Fibonacci 
--   numbers.
productFib :: Integer -> (Integer, Integer, Bool)
productFib n = helper n fibs