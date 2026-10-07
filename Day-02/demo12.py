# Demonstrate 5 common Python string methods
text = "  python programming is fun and easy!  "

print("Original text:", text)
print("1. strip() ->", text.strip())
print("2. upper() ->", text.upper())
print("3. lower() ->", text.lower())
print("4. replace() ->", text.replace("python", "Python"))
print("5. split() ->", text.strip().split())

# Extra example of find()
print("6. find('programming') ->", text.strip().find("programming"))
print("7. count('a') ->", text.strip().count("a"))
print("8. startswith('python') ->", text.strip().startswith("python"))
print("9. endswith('easy!') ->", text.strip().endswith("easy!"))
print("10. capitalize() ->", text.strip().capitalize())
print("11. title() ->", text.strip().title())
print("12. swapcase() ->", text.strip().swapcase())
print("13. isalpha() ->", text.strip().isalpha())
print("14. isdigit() ->", text.strip().isdigit())