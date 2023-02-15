module FriendOrFoe where

friend :: [String] -> [[Char]]
friend = filter (\x -> (length x) == 4) 