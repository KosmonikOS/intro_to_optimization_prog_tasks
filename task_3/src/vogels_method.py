import numpy as np


class VogelsMethod:
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
        differences = []
        valid_rows = [j for j in range(len(self.supply)) if self.supply[j] > 0]
        valid_cols = [i for i in range(len(self.demand)) if self.demand[i] > 0]
        for i in range(len(self.demand)):
            if self.demand[i] > 0:
                if len(valid_rows) > 1:
                    a, b = np.partition(self.costs[valid_rows, i], 1)[:2]
                    differences.append((b - a, "col", i))
                else:
                    differences.append((0, "col", i))
        for j in range(len(self.supply)):
            if self.supply[j] > 0:
                if len(valid_cols) > 1:
                    a, b = np.partition(self.costs[j, valid_cols], 1)[:2]
                    differences.append((b - a, "row", j))
                else:
                    differences.append((0, "row", j))
        _, _type, index = sorted(differences, key=lambda x: x[0], reverse=True)[0]

        if _type == "col":
            valid_costs = [(r, self.costs[r, index]) for r in valid_rows]
            min_row = min(valid_costs, key=lambda x: x[1])[0]
            return min_row, index
        else:
            valid_costs = [(c, self.costs[index, c]) for c in valid_cols]
            min_col = min(valid_costs, key=lambda x: x[1])[0]
            return index, min_col
