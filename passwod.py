import re

print("Password Strength Checker")
password = input("Enter your password: ")

# Check rules
length_ok = len(password) >= 8
has_number = re.search(r"\d", password) is not None
has_upper = re.search(r"[A-Z]", password) is not None
has_lower = re.search(r"[a-z]", password) is not None
has_symbol = re.search(r"[!@#$%^&*()_+=<>?/]", password) is not None

# Print rule results
print("\nPassword checks:")
print("✅ Length OK" if length_ok else "❌ Too Short")
print("✅ Has Number" if has_number else "❌ No Number")
print("✅ Has Uppercase" if has_upper else "❌ No Uppercase Letter")
print("✅ Has Lowercase" if has_lower else "❌ No Lowercase Letter")
print("✅ Has Symbol" if has_symbol else "❌ No Symbol")

# Final result
rules_passed = sum([length_ok, has_number, has_upper, has_lower, has_symbol])

print("\nOverall Password Strength:")
if rules_passed == 5:
    print("✅ Strong Password ")
elif rules_passed >= 3:
    print("🟡 Medium Password")
else:
    print("❌ Weak Password ")
