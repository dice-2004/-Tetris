import dataclasses
from typing import List, Any,Dict
@dataclasses.dataclass
class Kakin:
    base_point:int
    Tetromino:Dict[List[Any]] = {
        "I":[Any]
    }
