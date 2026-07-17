# 1. Even Numbers

# Generator function
def even_numbers(n):
    num = 2
    count = 0
    while count < n:
        yield num
        num += 2
        count += 1

# Decorator
def greet(func):
    def wrapper():
        print("Hello!")
        func()
    return wrapper


# Function with decorator
@greet
def introduce():
    print("My name is Alice")

n = int(input("Enter the value of n: "))

print("First", n, "even numbers:")
for i in even_numbers(n):
    print(i)


introduce()



# 2. Greetings and Text Analyzer 

import re

# Input text
text = "Email me at hello@example.com or admin@test.com. Call me at (123) 456-7890 or 987-654-3210. I love Python programming."

# 1. Find all email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)

print("Email Addresses:")
print(emails)

# 2. Find all phone numbers
phone_pattern = r'\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}'
phone_numbers = re.findall(phone_pattern, text)

print("\nPhone Numbers:")
print(phone_numbers)

# 3. Replace a word
new_text = text.replace("Python", "Java")

print("\nUpdated Text:")
print(new_text)