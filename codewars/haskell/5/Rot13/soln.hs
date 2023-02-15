module Rot13 where

import Data.Char

rotate modval rotateval offset n = ((n - offset + rotateval) `mod` modval) + offset
caesarRotate = rotate 26 13
rotateSmall = caesarRotate 97
rotateCaps= caesarRotate 65
isCaps ch = ord ch >= 65 && ord ch <= 90

helper ch = chr ((if isAscii ch && isLetter ch
            then (if isCaps ch then rotateCaps else rotateSmall)
            else id) (ord ch))

rot13 = map helper