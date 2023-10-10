def right_rotation(array, shift):
    for i in range(0, shift):
        temp = array[len(array)-1]
        for j in range(len(array)-1, 0, -1):
            array[j] = array[j-1]
        array[0] = temp

    return array

def print_array(array):
    for i in range(0, len(array)):
        print(array[i], end=' ')

input_string = input("Enter space-separated numbers: ")
arr = list(map(int, input_string.split()))

num_input = int(input("steps: "))

rotated_array = right_rotation(arr, num_input)
print_array(rotated_array)