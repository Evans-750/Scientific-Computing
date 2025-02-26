#creating  an integer
age=10

print(type(age))

#creating  a string

string="Lucas"
print(type(string))

#creating  a boolean

is_student=True
print(type(is_student))

#creating  a float

float=10.99
print(type(float))

#creating  a complex 

complex=2+5j
print(type(complex))

#creating  a list

list1=["Apples","Mangoes","Oranges",20]
print(type(list1))

tuple=("Grey","Yellow","Red",35)
print(type(tuple)) 

set=set(["car","aeroplane","bicycle",43,16])
print(type(set))

dict={1:"January",
      2:"February",
      3:"March"
     }
print(type(dict))

#converting from one datatype to another that is typecasting

age=float(age)
print(age)

string=complex(string)
print(string)

complex=string(complex)
print(complex)