input_number = int(input("Enter the number to find next smallest bigger number: "))
if len(str(input_number)) <= 2 :
    print("Not possible")
ones_digit = input_number % 10 
input_number = input_number // 10
tens_digit = input_number % 10
input_number = input_number // 10


smallest_bigger_number = (input_number * 100) + (ones_digit * 10) + tens_digit

print("Smallest Bigger Number: ", smallest_bigger_number)