# python3


def build_heap(data):
    swaps = []
    n = len(data)

    def rec_heapify(i):
        nonlocal swaps
        min_index = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and data[left] < data[min_index]:
            min_index = left

        if right < n and data[right] < data[min_index]:
            min_index = right

        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            rec_heapify(min_index)


    for i in range(n//2, -1, -1):
        rec_heapify(i)

    return swaps

def main():
    text = input("F or I: ")
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in text:
        file_name = input("Enter filename: ")
        file_path='./test/'
        file_full_name = file_path+file_name
        with open(file_full_name, "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
