def selection_sort(array):
    for i in range(len(array)):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
array = input("Enter a list of numbers, separated by commas: ").split(",")
array = [int(x) for x in array]
selection_sort(array)
print("The sorted list is:", array)
