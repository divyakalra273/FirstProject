def square(numbers):
    print("[Square]The numbers are",numbers, type(numbers), hex(id(numbers)))
    for i in range(0,len(numbers)):
        numbers[i]=numbers[i] * numbers[i]
    print("[Square]The numbers are", numbers, type(numbers), hex(id(numbers)))

numbers=[10,20,30,40,50]
print("[Main]The numbers are",numbers,type(numbers),hex(id(numbers)))
square(numbers)
