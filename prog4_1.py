
#CHECKn IF PALINDROME

#used string slicing and ternary opr

string=input("ENTER A STRING TO CHECK PALINDROME")

print(f"STRING:{string[0::]} REVERSE OF STRING :{string[::-1]}")

is_palindrome=True if (string[::-1]==string[0:]) else False

print(is_palindrome)

