import dataclasses
from typing import List, Dict, Literal


# 幅10、高さ20、左下原点の座標系上に描写
@dataclasses.dataclass
class hikakin:
    BASE: Dict[Literal["x", "y"], int]

    def __post_init__(self):
        self.Tetromino: Dict[str, List[List[int]]] = {
            # ex)    "D": [[x, y], [x, y], [x, y], [x, y]],
            "I": {
                "shaft": [self.BASE["x"], self.BASE["y"]],
                "tetro": [
                    [self.BASE["x"] - 1, self.BASE["y"]],
                    [self.BASE["x"], self.BASE["y"]],
                    [self.BASE["x"] + 1, self.BASE["y"]],
                    [self.BASE["x"] + 2, self.BASE["y"]],
                ],
            },
            "O": {
                "shaft": [self.BASE["x"], self.BASE["y"]],
                "tetro": [
                    [self.BASE["x"], self.BASE["y"]],
                    [self.BASE["x"] + 1, self.BASE["y"]],
                    [self.BASE["x"], self.BASE["y"] + 1],
                    [self.BASE["x"] + 1, self.BASE["y"] + 1],
                ],
            },
            "S": {
                "shaft": [self.BASE["x"], self.BASE["y"]],
                "tetro": [
                    [self.BASE["x"], self.BASE["y"]],
                    [self.BASE["x"] + 1, self.BASE["y"]],
                    [self.BASE["x"], self.BASE["y"] + 1],
                    [self.BASE["x"] - 1, self.BASE["y"] + 1],
                ],
            },
            "Z": {
                "shaft": [self.BASE["x"], self.BASE["y"]],
                "tetro": [
                    [self.BASE["x"], self.BASE["y"]],
                    [self.BASE["x"] - 1, self.BASE["y"]],
                    [self.BASE["x"], self.BASE["y"] + 1],
                    [self.BASE["x"] + 1, self.BASE["y"] + 1],
                ],
            },
            "J": {
                "shaft": [self.BASE["x"], self.BASE["y"]],
                "tetro": [
                    [self.BASE["x"], self.BASE["y"]],
                    [self.BASE["x"] - 1, self.BASE["y"]],
                    [self.BASE["x"] + 1, self.BASE["y"]],
                    [self.BASE["x"] + 1, self.BASE["y"] + 1],
                ],
            },
            "L": {
                "shaft": [self.BASE["x"], self.BASE["y"]],
                "tetro": [
                    [self.BASE["x"], self.BASE["y"]],
                    [self.BASE["x"] - 1, self.BASE["y"]],
                    [self.BASE["x"] + 1, self.BASE["y"]],
                    [self.BASE["x"] - 1, self.BASE["y"] + 1],
                ],
            },
            "T": {
                "shaft": [self.BASE["x"], self.BASE["y"]],
                "tetro": [
                    [self.BASE["x"], self.BASE["y"]],
                    [self.BASE["x"] - 1, self.BASE["y"]],
                    [self.BASE["x"] + 1, self.BASE["y"]],
                    [self.BASE["x"], self.BASE["y"] + 1],
                ],
            },
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
