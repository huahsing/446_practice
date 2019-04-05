def sort_by_numbers(item):
    return item[1]


cars = ['Ford', 'BMW', 'bMW', 'bmYEAdhad', 'Volvo']
# print(cars)
cars.sort()
# print(cars)

numbers = [10, 3, 378, 12, 57, 89, 4]
# print(numbers)
numbers.sort()
# print(numbers)

cars_numbers = [["Ford", 1007], ["BMW", 5678], ["Volvo", 1010]]
cars_numbers.sort()
print(cars_numbers)

cars_numbers.sort(reverse=True)
print(cars_numbers)

cars_numbers.sort(key=sort_by_numbers)
print(cars_numbers)
