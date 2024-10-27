import numpy as np


class RussellsMethod:
    def __init__(self, supply: np.array, demand: np.array, costs: np.array) -> None:
        self.supply = supply.copy()
        self.demand = demand.copy()
        self.costs = costs.copy()

    def solve(self) -> list[list[int]]:
        if sum(self.supply) != sum(self.demand):
            raise ValueError("The problem is not balanced!")

        result = [[0 for _ in range(len(self.demand))] for _ in range(len(self.supply))]

        while sum(self.supply) > 0 and sum(self.demand) > 0:
            x, y = self.find_next_cell()
            result[x][y] = min(self.supply[x], self.demand[y])
            self.supply[x] -= result[x][y]
            self.demand[y] -= result[x][y]
        return result

    def find_next_cell(self) -> tuple[int, int]:
        max_rows = [
            np.max(self.costs[j, :]) if self.supply[j] > 0 else -np.inf
            for j in range(len(self.supply))
        ]
        max_cols = [
            np.max(self.costs[:, i]) if self.demand[i] > 0 else -np.inf
            for i in range(len(self.demand))
        ]
        differences = np.array(
            [
                [
                    self.costs[i][j] - max_rows[i] - max_cols[j]
                    for j in range(len(self.demand))
                ]
                for i in range(len(self.supply))
            ]
        )
        return np.unravel_index(differences.argmin(), differences.shape)
