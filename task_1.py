def replace_missing_with_average(numbers):
    missing_index = numbers.index(None)
    total_sum = sum(numbers[:missing_index]) + sum(numbers[missing_index + 1:])
    count = len(numbers)
    average = total_sum / (count)
    numbers[missing_index] = average
    return numbers

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
updated_list = replace_missing_with_average(numbers)
print("Измененный список:", updated_list)
