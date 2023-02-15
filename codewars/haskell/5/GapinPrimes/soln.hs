module Codewars.G964.GapInPrimes where

isqrt = floor . sqrt . fromIntegral

isPrime k = if k > 1 then null [ x | x <- [2..isqrt k], k `mod` x == 0] else False

gap :: Integer -> Integer -> Integer -> Maybe (Integer, Integer)
gap g m n = let primes = [i | i <- [m..n], isPrime i]
                gapped = case primes of
                         [] -> []
                         otherwise -> [(x,y) | (x,y) <- zip primes (tail primes), y-x==g]
            in
              case gapped of
              [] -> Nothing
              (hd:_) -> Just hd