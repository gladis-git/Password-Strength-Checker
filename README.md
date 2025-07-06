# Password-Strength-Checker
•	Save the result of each check.
•	Count how many rules the password passed.
•	Give a final result: Weak, Medium, or Strong.
________________________________________
Step 1: Save Each Check in a Variable
This helps us store and reuse results.
import re

password = input("Enter your password: ")

length_ok = len(password) >= 8
has_number = re.search(r"\d", password) is not None
has_upper = re.search(r"[A-Z]", password) is not None
has_lower = re.search(r"[a-z]", password) is not None
has_symbol = re.search(r"[!@#$%^&*()_+=<>?/]", password) is not None
Let’s explain each:
Variable	Meaning
length_ok	True if password has 8+ characters
has_number	True if it has at least 1 digit
has_upper	True if it has at least 1 capital
has_lower	True if it has at least 1 small
has_symbol	True if it has at least 1 symbol
________________________________________
Step 2: Count How Many Conditions Are True
rules_passed = sum([length_ok, has_number, has_upper, has_lower, has_symbol])
Python counts True = 1 and False = 0, so sum() tells us how many rules passed.
________________________________________
Step 3: Give Final Strength
if rules_passed == 5:
    print(" Strong Password ")
elif rules_passed >= 3:
    print(" Medium Password ")
else:
    print(" Weak Password ")
