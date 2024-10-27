import numpy as np
class NorthWestMethod:
    def __init__(
        self, supply: np.array, demand: np.array, costs: np.array
    ) -> None:
        self.supply = supply.copy()
        self.demand = demand.copy()
        self.costs = costs.copy()

    def solve(self) -> list[list[int]]:
        if sum(self.supply) != sum(self.demand):
            raise ValueError("The problem is not balanced!")

        result = [[0 for _ in range(len(self.demand))] for _ in range(len(self.supply))]
        for i in range(len(self.supply)):
            for j in range(len(self.demand)):
                result[i][j] = min(self.supply[i], self.demand[j])
                self.supply[i] -= result[i][j]
                self.demand[j] -= result[i][j]
        return result
