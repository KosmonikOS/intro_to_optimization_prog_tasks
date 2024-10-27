import numpy as np
from north_west_method import NorthWestMethod
from vogels_method import VogelsMethod
from russells_method import RussellsMethod


def parse_input() -> tuple[np.array, np.array, np.array]:
    supply = np.array(
        list(map(int, input("Enter supply values separated by spaces: ").split()))
    )
    demand = np.array(
        list(map(int, input("Enter demand values separated by spaces: ").split()))
    )
    costs = np.array(
        [
            list(
                map(
                    int,
                    input(f"Enter costs for row {i+1} separated by spaces: ").split(),
                )
            )
            for i in range(len(supply))
        ]
    )
    return supply, demand, costs


def print_result(result: list[list[int]]):
    for row in result:
        print(row)


def print_problem(supply: np.array, demand: np.array, costs: np.array):
    for i in range(len(supply)):
        for j in range(len(demand)):
            print(f"{costs[i][j]:4d}", end="")
        print(f"|{supply[i]:2d}  ")
    print("-" * (len(demand) * 5 + 3))
    for j in range(len(demand)):
        print(f"{demand[j]:2d}", end=" ")
    print()


def main():
    supply, demand, costs = parse_input()
    print_problem(supply, demand, costs)
    north_west = NorthWestMethod(supply, demand, costs)
    north_west_result = north_west.solve()
    print("North-West Method:")
    print_result(north_west_result)
    vogels = VogelsMethod(supply, demand, costs)
    vogels_result = vogels.solve()
    print("Vogel's Method:")
    print_result(vogels_result)
    russells = RussellsMethod(supply, demand, costs)
    russells_result = russells.solve()
    print("Russells Method:")
    print_result(russells_result)


if __name__ == "__main__":
    main()