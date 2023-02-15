module Haskell.SylarDoom.Smallfuck where
import Data.List
import Debug.Trace

--  the list-zipper of [1, 2, 3, 4] at the location of "3" may be represented as ([2, 1], [3, 4])

-- bool indicates success in forwarding. Failure is when matching ] is not found
-- the Int takes care of nesting
forward :: String -> String -> Int -> (String, String, Bool)
forward topCode [] _ = (topCode, [], False)
forward topCode (currCode:bottomCode) cnt = let nextCall = forward (currCode:topCode) bottomCode
                                        in
                                          case (currCode,cnt) of
                                          (']',0) -> ((currCode:topCode), bottomCode, True)
                                          (']',cnt) -> nextCall (cnt-1)
                                          ('[',cnt) -> nextCall (cnt+1)
                                          otherwise -> nextCall cnt

backward :: String -> String -> Int -> (String, String, Bool)
backward [] (currCode:bottomCode) cnt = ([], (currCode:bottomCode), currCode == '[' && cnt == 0)
backward topCode (currCode:bottomCode) cnt = let nextCall = backward (tail topCode) ((head topCode):(currCode:bottomCode))
                                        in
                                          case (currCode,cnt) of
                                          ('[',0) -> ((currCode:topCode), bottomCode, True)
                                          ('[',cnt) -> nextCall (cnt-1)
                                          (']',cnt) -> nextCall (cnt+1)
                                          otherwise -> nextCall cnt

flipBit x = (if x == '0' then '1' else '0')

helper :: String -> String -> String -> String -> String


helper _ [] t1 t2 = (reverse t1) ++ t2 -- All commands have been considered from left to right
helper topCode (currCode:bottomCode) topTape (currTape:bottomTape) = 
  let
    fullTape = (reverse topTape) ++ [currTape] ++ bottomTape
    nextCall = helper (currCode:topCode) bottomCode
  in
    case currCode of
    '>' -> if length bottomTape == 0 
           then fullTape
           else nextCall (currTape:topTape) bottomTape
    '<' -> if length topTape == 0
           then fullTape
           else nextCall (tail topTape) ((head topTape) : currTape : bottomTape)
    '*' -> nextCall topTape ((flipBit currTape):bottomTape)
    '[' -> if currTape == '0'
           then case forward topCode (currCode:bottomCode) (-1) of
                  (_,_,False) -> fullTape
                  (newTopCode, newBottomCode, True) -> helper newTopCode newBottomCode topTape (currTape:bottomTape)
           else nextCall topTape (currTape:bottomTape)
    ']' -> if currTape == '0'
           then helper (currCode:topCode) bottomCode topTape (currTape:bottomTape)
           else  case backward topCode (currCode:bottomCode) (-1) of
                   (_,_,False) -> fullTape
                   (newTopCode, newBottomCode, True) -> helper newTopCode newBottomCode topTape (currTape:bottomTape)
    otherwise -> nextCall topTape (currTape:bottomTape)


interpreter :: String -> String -> String
interpreter code tape =  (helper [] code [] tape)
--trace (if length tape == 256 then (code ++ "   " ++ tape) else "")