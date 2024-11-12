numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
filtered_numbers = [2, -93, -2, 8, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
total_sum = sum(filtered_numbers)
count_with_none = len(numbers)
average = total_sum / (count_with_none)

numbers[numbers.index(None)] = average
print("Измененный список:", numbers)
