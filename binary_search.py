def binary_search(data,needle,key=None):
    left_index=0
    right_index=len(numbers)

    while right_index - left_index>1:
        middle_index=(right_index-left_index) // 2 + left_index
        print(middle_index)
        if key:
            datum=key(data[middle_index])
        if datum>needle:
            right_index=middle_index
        elif datum<needle:
            left_index=middle_index
        else:
            return middle_index


def main(needle):
    with open("Data/data_nums_1000000.txt","r") as file:
        numbers=list(map(int,file.read().splitlines()))
        numbers.sort()
        with open("data_nums_sorted.txt", "w") as file2:
            for n in numbers:
                file2.write(f"{n}\n")

