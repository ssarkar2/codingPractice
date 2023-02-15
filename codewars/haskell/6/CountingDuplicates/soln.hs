module Codwars.Kata.Duplicates where
import Data.Char

import Data.List
duplicateCount :: String -> Int
duplicateCount inp = let 
                        lowered = [ toLower x | x <- inp]
                        (unique, dup) = foldl (\(unique, dup) x -> if x `elem` unique 
                                                   then
                                                    if x `elem` dup
                                                    then (unique, dup)
                                                    else (unique, x:dup)
                                                   else (x:unique, dup)) ([],[]) lowered
                      in
                        length dup