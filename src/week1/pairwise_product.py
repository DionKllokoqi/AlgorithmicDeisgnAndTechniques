# Uses python3


def get_maximum_pairwise_product(numbers):
    largest, largest_index = -1, 0
    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
            largest_index = i

    second_largest = -1
    for i in range(len(numbers)):
        if i != largest_index and numbers[i] > second_largest:
            second_largest = numbers[i]

    return largest * second_largest


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(get_maximum_pairwise_product(input_numbers))
