try:
    val_1 = int(input("Enter value 1: "))
except:
    print("Error: Value is not a number:")
    print("Handling by using 0 as number")
    val_1 = 0

try:
    val_2 = int(input("Enter Value 2: "))
except:
    print("Error: Value is not a number:")
    print("Handling by using 0 as number")
    val_2 = 0

try:
    val_3 = int(input("Enter value 3: "))
except:
    print("Error: Value is not a number")
    print("Handling by using 0 as a number")
    val_3 =0

def add(a, b):
    c= a + b
    print("Result of addition is: ", c)
    return c

print("Runnig add function with values: ", val_1, val_2)
answer = add(val_1,val_2)
print("Add function executed successfully")

print("Running add function with values: ", answer, val_3)
add(answer, val_3)
print("Add function executed successfully")