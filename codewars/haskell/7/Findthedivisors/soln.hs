module Divisors where


divisors :: (Show a, Integral a) => a -> Either String [a]
divisors k = case tmp of 
              [] -> Left ((show k) ++ " is prime")
              otherwise -> Right tmp
             where
              tmp = [ x | x <- [2..k-1],  k `rem` x == 0]