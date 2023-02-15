module MaxSequence where

-- Return the greatest subarray sum within the array of integers passed in.

maxSequence :: [Int] -> Int
maxSequence arr = let maximum = foldr1 (\x y ->if x >= y then x else y)
                  in maximum (scanl (\acc x -> max x (x+acc)) 0 arr)