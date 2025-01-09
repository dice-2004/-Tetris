import dataclasses
from typing import List, Dict,Literal

# 幅10、高さ20、左下原点の座標系上に描写
@dataclasses.dataclass
class Defalut:
    SHAFT:Dict[Literal["x","y"],int]
    def __post_init__(self):
        self.Tetromino: Dict[str, List[List[int]]] ={
    #ex)    "D": [[x, y], [x, y], [x, y], [x, y]],
            "I": [
                [self.SHAFT["x"] - 1, self.SHAFT["y"]],
                [self.SHAFT["x"], self.SHAFT["y"]],
                [self.SHAFT["x"] + 1, self.SHAFT["y"]],
                [self.SHAFT["x"] + 2, self.SHAFT["y"]]
                ],
            "O": [
                [self.SHAFT["x"], self.SHAFT["y"]],
                [self.SHAFT["x"] + 1, self.SHAFT["y"]],
                [self.SHAFT["x"], self.SHAFT["y"] +1],
                [self.SHAFT["x"] + 1, self.SHAFT["y"] +1]
                ],
            "S": [
                [self.SHAFT["x"], self.SHAFT["y"]],
                [self.SHAFT["x"] + 1, self.SHAFT["y"]],
                [self.SHAFT["x"] + 1, self.SHAFT["y"] + 1],
                [self.SHAFT["x"] + 2, self.SHAFT["y"] + 1]
                ],
            "Z": [
                [self.SHAFT["x"] + 1, self.SHAFT["y"]],
                [self.SHAFT["x"] + 2, self.SHAFT["y"]],
                [self.SHAFT["x"], self.SHAFT["y"] + 1],
                [self.SHAFT["x"] + 1, self.SHAFT["y"] + 1]
                ],
            "J": [
                [self.SHAFT["x"]+1, self.SHAFT["y"]],
                [self.SHAFT["x"]+1, self.SHAFT["y"]+1],
                [self.SHAFT["x"]+1, self.SHAFT["y"]+2],
                [self.SHAFT["x"], self.SHAFT["y"]+2]
                ],
            "L": [
                [self.SHAFT["x"], self.SHAFT["y"]],
                [self.SHAFT["x"], self.SHAFT["y"]+1],
                [self.SHAFT["x"], self.SHAFT["y"]+2],
                [self.SHAFT["x"]+1, self.SHAFT["y"]+2]
                ],
            "T": [
                [self.SHAFT["x"]-1, self.SHAFT["y"]],
                [self.SHAFT["x"], self.SHAFT["y"]],
                [self.SHAFT["x"]+1, self.SHAFT["y"]],
                [self.SHAFT["x"], self.SHAFT["y"]+1]
                ]
        }

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
