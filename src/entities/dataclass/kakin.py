import dataclasses
from typing import List, Dict

BASE:Dict[str,int] = {"x":5,"y":20}


# 幅10、高さ20、左上原点の座標系上に描写
@dataclasses.dataclass
class Kakin:
    Tetromino:Dict[str,List[List[int]]] = dataclasses.field(default_factory=lambda:{
#ex)    "D": [[x, y], [x, y], [x, y], [x, y]],
        "I":[
            [BASE["x"]-1,BASE["y"]],
            [BASE["x"],BASE["y"]],
            [BASE["x"]+1,BASE["y"]],
            [BASE["x"]+2,BASE["y"]]
            ]
    })

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
