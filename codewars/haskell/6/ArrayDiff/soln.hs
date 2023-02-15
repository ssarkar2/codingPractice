module Difference where
import Data.List
removeItem xs []                 = xs
removeItem [] _                  = []
removeItem (x:xs) ys | x `elem` ys = removeItem xs ys
                     | otherwise = x : removeItem xs ys

difference :: Eq a => [a] -> [a] -> [a]
difference a b = removeItem a (nub b)