number=int(input("Enter a number:"))

if number % 2 ==0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd")
    
even_numbers=[]

for numbers in range(1,51):
    if numbers % 2 == 0:
        even_numbers.append(numbers)
        print(even_numbers)
        
        number1=10
        while number1 >=1:
            print(number1)
            number1 -= 1
            
def classify_number(number):
    if number % 2==0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."