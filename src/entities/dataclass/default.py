import dataclasses
from typing import List, Dict

BASE: Dict[str, int] = {"x": 5, "y": 20}


# 幅10、高さ20、左下原点の座標系上に描写
@dataclasses.dataclass
class Defalut:
    Tetromino: Dict[str, List[List[int]]] = dataclasses.field(default_factory=lambda: {
#ex)    "D": [[x, y], [x, y], [x, y], [x, y]],
        "I": [BASE["x"] - 1, BASE["y"], BASE["x"], BASE["y"], BASE["x"] + 1, BASE["y"], BASE["x"] + 2, BASE["y"]],
        "O": [[BASE["x"], BASE["y"]], [BASE["x"] + 1, BASE["y"]], [BASE["x"], BASE["y"] + 1], [BASE["x"] + 1, BASE["y"] + 1]],
        "S": [[BASE["x"], BASE["y"]], [BASE["x"] + 1, BASE["y"]], [BASE["x"] + 1, BASE["y"] + 1], [BASE["x"] + 2, BASE["y"] + 1]],
        "Z": [[BASE["x"] + 1, BASE["y"]], [BASE["x"] + 2, BASE["y"]], [BASE["x"], BASE["y"] + 1], [BASE["x"] + 1, BASE["y"] + 1]],
        "J": [[BASE["x"]+1, BASE["y"]], [BASE["x"]+1, BASE["y"]+1], [BASE["x"]+1, BASE["y"]+2], [BASE["x"], BASE["y"]+2]],
        "L": [[BASE["x"], BASE["y"]], [BASE["x"], BASE["y"]+1], [BASE["x"], BASE["y"]+2], [BASE["x"]+1, BASE["y"]+2]],
        "T": [[BASE["x"]-1, BASE["y"]], [BASE["x"], BASE["y"]], [BASE["x"]+1, BASE["y"]], [BASE["x"], BASE["y"]+1]]
    })

# 20
# 19
# 18
# 17
# 16
# 15
# 14
# 13
# 12
# 11
# 10
#  9
#  8
#  7
#  6
#  5
#  4
#  3
#  2
#  1,2,3,4,5,6,7,8,9,10
