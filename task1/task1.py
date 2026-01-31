grades = [85, 92, 78, 90, 85, 88, 92, 78, 85, 90]

print('--- Program start ---')

def average_finder(input_list: list) -> float:
    return sum(input_list) / len(input_list)

def create_distribution(input_list: list) -> dict:
    output_dictionary = dict.fromkeys(input_list, 0)
    for item in input_list:
        output_dictionary[item] += 1
    return output_dictionary

def high_values_finder(input_list: list, bottom_limit: int) -> set:
    high_values = set()
    high_values = set(filter(lambda x: x > bottom_limit, input_list))
    return high_values

average = average_finder(grades)

max_grade = max(grades)
min_grade = min(grades)

distribution = create_distribution(grades)

high_grades = high_values_finder(grades, 85)

results = {'average': average, 'max': max_grade, 'min': min_grade, 'distribution': distribution, 'high_grades': high_grades}

print(results)

print('--- Program end ---')