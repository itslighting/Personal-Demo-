# Calculator
First Repository.
<br>
Author - Ajay Biswas
<br>
I am create a calculator using python.
<br>
Hope You Enjoy :)

```python
It can do addition, subtraction, multiplication, division,
a = int(input("Enter the first number: ") or 0)  # Convert input to integer.
b = int(input("Enter the second number: ") or 0) # Convert input to integer.
c = int(float(input("Enter the modulus number: ")) or 0) # Convert input to integer.
d = 0.1 #Assign a specific value to a variable.
```

```python
print("The Addition value of ", a, "+", b, "is:-" ,(int(a) + int(b))) # Assign a specific value to a variable.

print ("The Subtraction value of", a, "-", b, "is:-" ,(int(a) - int(b))) # Assign a specific value to a variable.

print ("The Multiplication value of", a, "*", b, "is:-" ,(int(a) * int(b))) # Assign a specific value to a variable.

def Error_Fixing(a, b): #This is a function (/)
    if b < 0:
        print("The Division value of", a, "/", b, "is:-", (int(a) / int(b)))
    else:
        print("Error") #Cannot divide by zero! Please enter a non-zero value for the second number.

def Erro_Fixing(a, b): #This is a function (//)
    if b < 0:
        print("The Floor Division value of", a, "//", b, "is:-", (int(a) // int(b)))
    else:
        print("Error") #Cannot divide by zero! Please enter a non-zero value for the second number.
print ("The Modulus value of", a, "%", c, "is:-" ,(int(a) % int(c)))
```
