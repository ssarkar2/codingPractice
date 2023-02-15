module Codewars.G964.Josephus where

deleteAt idx xs = lft ++ rgt
  where (lft, (_:rgt)) = splitAt idx xs

{-helper :: Int -> Int -> [Int] -> (Int, [Int])
helper k startidx (hd:[]) = (0,[hd])
helper k startidx lst = let delidx = (startidx + k - 1) `rem` (length lst)
                        in (delidx, deleteAt delidx lst)

doAllRounds :: Int -> Int -> [Int] -> Int
doAllRounds k startidx lst = let
                                (startidxNew, remaining) = helper k startidx lst
                             in
                                if length remaining == 1
                                then head remaining
                                else doAllRounds k startidxNew remaining



josephusSurvivor :: Int -> Int -> Int
josephusSurvivor n k = (doAllRounds k 0 [0..n-1]) + 1
-}

josephusSurvivor 1 _ = 1
josephusSurvivor n k = (((josephusSurvivor (n-1) k) + k - 1) `mod` n) + 1