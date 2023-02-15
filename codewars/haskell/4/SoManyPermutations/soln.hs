module Codewars.Kata.Permutations (permutations) where
import Data.List (nub)
inserter ch st idx = let (top, bot) = splitAt idx st
                     in top ++ [ch] ++ bot 

addToAll :: Char -> String -> [String]
addToAll ch st = map (inserter ch st) [0..length st]

flat = foldl (++) []

permutations :: String -> [String]
permutations [] = [""]
permutations (hd:tl) = (nub . flat) (map (addToAll hd) $ permutations tl)