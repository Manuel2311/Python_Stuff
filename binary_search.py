from typing import Any, Optional, Callable, Union, Text

def binary_search(data,needle,key=None):
    left_index=0
    right_index=len(data)

    while right_index - left_index>1:
        middle_index=(right_index-left_index) // 2 + left_index
        print(middle_index)
        if key:
            datum=key(data[middle_index])
        else:
            datum=data[middle_index]
        if datum>needle:
            right_index=middle_index
        elif datum<needle:
            left_index=middle_index
        else:
            return middle_index + 1     

def main(needle):
    with open("Data/data_nums_1000000.txt","r") as file:
        numbers=list(map(int,file.read().splitlines()))
        numbers.sort()
        with open("data_nums_sorted.txt", "w") as file2:
            for n in numbers:
                file2.write(f"{n}\n")

assert binary_search([4,8,15,16,23,42],15)==2,"OMG THE WORLD IS ON FIRE"

if __name__ == "__main__":
    pass