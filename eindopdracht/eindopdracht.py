print("selecteer een print:")
print("1. PLUS")
print("2. AFTREKKEN")
print("3. VERMENIGVULDIGEN")
print("4. VERDELING")

operation = input()

if operation == "1":
    num1 = input("Kies een nummer: ")
    num2 =input("Kies een tweede nummer: ")
    print("De som is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Kies een nummer: ")
    num2 =input("Kies een tweede nummer: ")
    print("Het verschil is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Kies een nummer ")
    num2 =input("Kies een tweede nummer: ")
    print("Het antwoord is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Kies een nummer: ")
    num2 =input("Kies een tweede nummer: ")
    print("Het resultaat is " + str(int(num1) / int(num2)))
else:
    print("syntax error")