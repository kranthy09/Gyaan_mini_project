from typing import List


class InvalidPostId(Exception):
    pass


class InvalidUserId(Exception):
    pass


class InvalidOffset(Exception):
    pass

class InvalidLimit(Exception):
    pass

class InvalidPostIds(Exception):
    def __init__(self, invalids: List[int]):
        self.invalids = invalids