module Solution where

oddRow :: Integer -> [Integer]
oddRow n = let
            startOdd = n * (n-1) `div` 2
           in
            [2*x+1 | x <- [startOdd..startOdd+n-1]]