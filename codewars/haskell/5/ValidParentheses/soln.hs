module Codewars.Parentheses where
import Data.Maybe

helper1 (Just 0) ')' = Nothing
helper1 acc x = case acc of
                Nothing -> Nothing
                Just a -> Just (a + (if x=='(' then 1 else -1))


validParentheses :: String -> Bool
validParentheses x = case foldl helper1 (Just 0) x of
                     Just 0 -> True
                     otherwise -> False