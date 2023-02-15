module Codewars.Kata.Bus where

number :: [(Int, Int)] -> Int
number [] = 0
number ((a,b):rest) = a - b + number rest
