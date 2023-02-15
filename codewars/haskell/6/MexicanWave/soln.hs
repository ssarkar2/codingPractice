module MexicanWave where
import Data.Char
import Data.List

 

wave :: String -> [String]
wave s = let 
            helper idx = let
                          (top,bot) = splitAt idx s
                         in
                          top ++ [toUpper (head bot)] ++ (tail bot)
            waveWithspace = map helper [0..(length s)-1]
         in 
              filter (\x-> (map toLower x) /= x) waveWithspace