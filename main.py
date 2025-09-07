from flatten import flatten


def main():
    # Basic usage
    result = flatten([1, [2, [3, 4]], 5])
    print(result)  # [1, 2, 3, 4, 5]

    # Handle empty lists
    result = flatten([[], [1, []], [2]])
    print(result)  # [1, 2]

    # Work with negative numbers
    result = flatten([-1, [0, [-2, [3]]]])
    print(result)  # [-1, 0, -2, 3]


if __name__ == "__main__":
    main()