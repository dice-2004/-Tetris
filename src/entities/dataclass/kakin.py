import dataclasses
from typing import List, Dict,Literal


# 幅10、高さ20、左上原点の座標系上に描写
@dataclasses.dataclass
class Kakin:
    SHAFT:Dict[Literal["x","y"],int]

    def __post_init__(self):
        self.Tetromino:Dict[str,List[List[int]]] = {
    #ex)    "D": [[x, y], [x, y], [x, y], [x, y]],
            "I": [
                [self.SHAFT["x"] - 1, self.SHAFT["y"]],
                [self.SHAFT["x"], self.SHAFT["y"]],
                [self.SHAFT["x"] + 1, self.SHAFT["y"]],
                [self.SHAFT["x"] + 2, self.SHAFT["y"]]
                ],
        }

#  0,1,2,3,4,5,6,7,8,9
#  1
#  2
#  3
#  4
#  5
#  6
#  7
#  8
#  9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
