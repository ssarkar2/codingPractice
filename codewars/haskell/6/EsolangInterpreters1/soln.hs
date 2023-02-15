module MiniStringFuck where

import Data.Char

myFirstInterpreter :: String -> String
myFirstInterpreter code = snd (foldl (\(accCount, accString) x -> case x of
                                            '+' -> ((accCount+1) `mod` 256, accString)
                                            '.' -> (accCount, accString ++ [chr accCount])
                                            otherwise -> (accCount, accString)) (0,"") code)