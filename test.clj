(def inited-row (vec (take 5 (repeat 0))))
(def inited-board (vec (take 5 (repeat inited-row))))
(defn init-player [column player-id board] (
  let
  [splited-board (split-at column board)]
  (into
    (first splited-board)
    (cons
      (vec
        (take 
          (count (first board))
          (repeat player-id)))
      (rest (last splited-board))))))
(def init-players (
  (init-player 0 1 (init-player 4 2 inited-board))))
(defn init-multi-zero-vec [x]
    (if (= 0 (count x))
      0
      (vec (take (first x)
        (repeat
          (init-multi-zero-vec (rest x)))))))