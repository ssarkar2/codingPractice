module Codewars.G964.WeightSort where
import Data.List
import Data.Char
import Data.String
data NumSpecial = NumSpecial String deriving (Show)



weight = sum . (map digitToInt)

instance Eq NumSpecial where
  (==) (NumSpecial x) (NumSpecial y) = (weight x) == (weight y) && (x == y)

instance Ord NumSpecial where
  (<=) (NumSpecial x) (NumSpecial y) = if (weight x) == (weight y)
                                       then x <= y
                                       else (weight x) <= (weight  y)


split :: [Char] -> [[Char]]
split = foldr (\x acc -> case x of
                         ' ' -> if (length . head) acc == 0 then acc else []:acc
                         otherwise -> (x:(head acc)) : tail acc) [[]]


join  = tail . (foldr (\x acc -> acc ++ " " ++ x) "")

--orderWeight :: [Char] -> [Char]
--orderWeight strng = strng
  --your code
orderWeight :: [Char] -> [Char]
orderWeight inp = join [x | NumSpecial x <- (reverse . sort . (map NumSpecial) . split)  inp]