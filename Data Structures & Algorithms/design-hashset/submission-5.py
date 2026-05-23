class MyHashSet:
    def __init__(self):
        # Create an array of 1,000,001 False values
        self.hash_set = [False] * 1000001

    def add(self, key: int) -> None:
        self.hash_set[key] = True

    def remove(self, key: int) -> None:
        self.hash_set[key] = False

    def contains(self, key: int) -> bool:
        return self.hash_set[key]