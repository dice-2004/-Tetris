import dataclasses
from typing import List, Any,Dict
@dataclasses.dataclass
class Tetromino:
    base_point:int
    Tetromino:Dict[List[Any]] = {
        "I":[Any],
        "O":[Any],
        "S":[Any],
        "Z":[Any],
        "J":[Any],
        "L":[Any],
        "T":[Any]

    }
