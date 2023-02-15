module SumOfIntervals (sumOfIntervals) where

-- checked, is correct
-- x is covered by y
isDominated :: (Int, Int) -> (Int, Int) -> Bool
isDominated (fstx, sndx) (fsty, sndy) = (fstx >= fsty) && (sndx <= sndy)

-- checked, is correct
-- there exists an interval in intvls that completely covers/dominates intvl
dominatorExists :: (Int, Int) -> [(Int, Int)] -> Bool
dominatorExists intvl intvls = any (isDominated intvl) intvls

-- checked, is correct
removeDominated :: (Int, Int) -> [(Int, Int)] -> [(Int, Int)]
removeDominated intvl intvls = filter (not . (flip isDominated) intvl) intvls

-- i1 and i2 are overlapping 
fuse :: (Int, Int) -> (Int, Int) -> (Int, Int)
fuse (fstx, sndx) (fsty, sndy) = (min fstx fsty, max sndx sndy)

isOverlapped (fstx, sndx) (fsty, sndy) = ((min sndx sndy) - (max fstx fsty)) >= 0

reduceOne :: (Int, Int) -> [(Int, Int)] -> [(Int, Int)]
reduceOne intvl intvls = if dominatorExists intvl intvls
                         then intvls
                         else 
                            let
                              tmp = removeDominated intvl intvls
                              partialOverLapFst = filter (\(f,s) -> (s >= fst intvl) && (f <= fst intvl)) tmp
                              partialOverLapSnd = filter (\(f,s) -> (f <= snd intvl) && (s >= snd intvl)) tmp
                              noOverlap = filter (not . (isOverlapped intvl)) tmp
                            in
                              case (partialOverLapFst, partialOverLapSnd) of
                              ([],[]) -> intvl : noOverlap
                              ([],(x:[])) -> (fuse intvl x) : noOverlap
                              ((x:[]),[]) -> (fuse intvl x) : noOverlap
                              ((x:[]),(y:[])) -> (fuse y (fuse intvl x)) : noOverlap

reduceIntervals :: [(Int, Int)] -> [(Int, Int)]
reduceIntervals = foldl (flip reduceOne) []

sumOfIntervals :: [(Int, Int)] -> Int
sumOfIntervals = sum . (map (\(x,y) -> y-x)) . reduceIntervals

--sumOfIntervals = reduceIntervals
