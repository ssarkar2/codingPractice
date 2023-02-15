module Codewars.G.Persistence where
import Data.Char

digits :: Int -> [Int]
digits = (map digitToInt) . show

listProd :: [Int] -> Int
listProd = foldl (*) 1

helper :: Int -> Int -> Int
helper acc n = let
                 digs = digits n
               in if length digs == 1 then acc else helper (acc+1) (listProd digs)

persistence :: Int -> Int
persistence = helper 0