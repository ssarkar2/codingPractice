module Codewars.G964.Sumdivsq where

divisors n = [x | x <- [1..n], n `mod` x == 0]
sumOfSquares = foldl (\acc x -> acc + (x*x)) 0
isSquare n = sq * sq == n
    where sq = floor $ sqrt $ (fromIntegral n::Double)

listSquared :: Int -> Int -> [(Int, Int)]
listSquared m n = foldr (\x acc -> let
                                      sm = sumOfSquares (divisors x)
                                    in
                                      if isSquare sm then (x,sm):acc else acc) [] [m..n]

{-if m==n
                  then []
                  else 
                    let 
                      sm = sumOfSquares (divisors m)
                      rst = listSquared (m+1) n
                    in
                      if isSquare sm
                      then (m, sm) : rst
                      else rst
                      -}