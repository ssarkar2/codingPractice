module CreatePhoneNumber where
import Data.Char
createPhoneNumber :: [Int] -> String
intArrToString nums = map chr (map (+ 48) nums)
createPhoneNumber nums = let 
                          tmp = intArrToString nums
                          first = take 3 tmp
                          midlast = drop 3 tmp
                          mid = take 3 midlast
                          last = drop 3 midlast
                         in "(" ++ first ++ ") " ++ mid ++ "-" ++ last