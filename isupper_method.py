string = "Ah! Hi!"

# how isupper() works
for char in string:
    print(f"Is '{char}' uppercase? {char.isupper()}")

# how isupper() works without isupper() method
for char in string:
    if 'A' <= char <= 'Z':
        print(f"Is '{char}' uppercase? True")
    else:
        print(f"Is '{char}' uppercase? False")