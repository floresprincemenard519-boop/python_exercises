email_address = "me.@gmail.com"
second_email_address = "you.@gmail.com"
not_a_gmail_address = "me.@yahoo.com"

# how endswith() works
print(f"Is '{email_address}' a gmail address? {email_address.endswith('@gmail.com')}")

# how endswith() works without endswith() method
if "@gmail.com" in not_a_gmail_address[-10:]:
    print(f"Is '{not_a_gmail_address}' a gmail address? True")
else:
    print(f"Is '{not_a_gmail_address}' a gmail address? False")