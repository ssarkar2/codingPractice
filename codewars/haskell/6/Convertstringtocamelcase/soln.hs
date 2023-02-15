module CamelCase where
import Data.Char
toCamelCase :: String -> String
toCamelCase [] = []
toCamelCase "-" = []
toCamelCase "_" = []
toCamelCase str = let
                    aug = "x" ++ str
                    detectJoin x = elem x ['_', '-']
                  in 
                    [if (detectJoin prev) then toUpper x else x | (prev, x) <- zip aug (tail aug), not $ detectJoin x]