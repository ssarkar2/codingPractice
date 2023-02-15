module LastDigit where

lastDig :: Integer -> Integer
lastDig n = n `mod` 10

accessListIdx lst 0 = head lst
accessListIdx (_:rst) idx = accessListIdx rst (idx-1)

helper :: Integer -> Integer -> Integer
helper lasta b = let
                cache = [[0], [1], [2,4,8,6], [3,9,7,1], [4,6], [5], [6], [7,9,3,1], [8,4,2,6], [9,1]]
                series = accessListIdx cache lasta--cache !! lasta
              in
                accessListIdx series ((b-1) `mod` toInteger (length series))
                --series !! (b `mod` (length series))


lastDigit :: Integer -> Integer -> Integer
lastDigit a 0 = 1
lastDigit a b = helper (lastDig a) b