module Codewars.Kata.Square where
import Data.List

isSquare :: Integral n => n -> Bool
isSquare n = case find (\x -> x*x == n) [0..(n `div` 2) + 1] of
                  Nothing -> False
                  Just _ -> True