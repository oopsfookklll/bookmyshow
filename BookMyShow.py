```python
class BookMyShow:
    def __init__(self, n, m):
        self.hall = [[0]*m for _ in range(n)]

    def gather(self, k, maxRow):
        for r in range(maxRow + 1):
            for c in range(len(self.hall[r]) - k + 1):
                if all(self.hall[r][c+i] == 0 for i in range(k)):
                    for i in range(k):
                        self.hall[r][c+i] = 1
                    return [r, c]
        return []

    def scatter(self, k, maxRow):
        seats = []
        for r in range(maxRow + 1):
            for c in range(len(self.hall[r])):
                if self.hall[r][c] == 0:
                    seats.append((r, c))
                    if len(seats) == k:
                        for r, c in seats:
                            self.hall[r][c] = 1
                        return True
        return False
```