module OfficeV (meeting) where

meeting :: [(String,Int)] -> Int -> Either String [Int]
meeting rooms 0 = Left "Game On"
meeting rooms n = let
                    helper :: [(String,Int)] -> Int -> (Int, [Int])
                    helper [] n = (0,[])
                    helper ((occupants, chairs):rest) n = if n>0 then
                                                          let supply = max (chairs - length(occupants)) 0
                                                          in 
                                                            if n < supply 
                                                            then (n, [n])
                                                            else
                                                              let (tot,supplyPlan) = helper rest (n-supply)
                                                              in
                                                                (tot + supply, (supply:supplyPlan))
                                                        else
                                                          (0,[])
                  in
                    let
                      (tot,supplyPlan) = helper rooms n
                    in
                      if tot < n then Left "Not enough!" else Right supplyPlan