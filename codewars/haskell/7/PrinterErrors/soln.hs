module Codewars.G964.Printer where

printerError :: [Char] -> [Char]
printerError s = show(length $ filter (\x -> not $ elem x ['a'..'m']) s) ++ "/" ++ show(length s)