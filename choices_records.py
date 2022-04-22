# from collections import defaultdict
from dataclasses import dataclass, field

@dataclass
class ChoicesRecords:
    choices = dict()
    # dict[int, str] = field(default_factory=defaultdict[int, str])  # user_id : switch_type
