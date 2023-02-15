module DescendingOrder where
import Data.List
descendingOrder :: Integer -> Integer



descendingOrder n = let
                      splitter 0 =  []
                      splitter n = n `mod` 10: splitter (n `div` 10) 
                      digits = splitter n
                      joiner digits_ = sum [digit*10^(idx-1) | (idx, digit) <- zip [1..] digits_]
                    in joiner $ sort digits