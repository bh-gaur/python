import re  # 're' module is used to work with Regular Expressions (regex) in Python

# ==============================================================================
# 1. Finding a Word in a Sentence
# ==============================================================================
text = "I am learning Python"
check = re.search(r"Python", text)  # Looks for the word "Python"

if check:
    print("Pattern found in the text")
else:
    print("Pattern not found")

# ✅ Explanation:
# re.search(pattern, text) → Searches for "Python" anywhere in the string.


# ==============================================================================
# 2. Finding a Number in a Sentence
# ==============================================================================
text = "My favorite number is 42."
match = re.search(r"\d+", text)  # Looks for one or more digits

if match:
    print("Found number:", match.group())
else:
    print("Number not found")

# ✅ Explanation:
# \d+ → Matches one or more digits (e.g., 42).
# match.group() → Returns the first found number.


# ==============================================================================
# 3. Checking if an Email is Valid
# ==============================================================================
email = "user@example.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.match(pattern, email):
    print("Valid email!")
else:
    print("Invalid email!")

# ✅ Explanation:
# ^ → Start of the string.
# [a-zA-Z0-9_.+-]+ → Letters, numbers, and allowed symbols before @.
# @ → Must contain @.
# [a-zA-Z0-9-]+ → Domain name (e.g., example).
# \.[a-zA-Z0-9-.]+$ → Ends with dot and top-level domain (e.g., .com).


# ==============================================================================
# 4. Extracting a Date from a Sentence
# ==============================================================================
text = "The event is on 15/08/2025."
date = re.search(r"\d{2}/\d{2}/\d{4}", text)

if date:
    print("Found date:", date.group())  # Output: 15/08/2025

# ✅ Explanation:
# \d{2}/\d{2}/\d{4} → Finds a date in dd/mm/yyyy format.


# ==============================================================================
# 5. Checking if a Phone Number is Valid
# ==============================================================================
phone_number = "(123) 456-7890"
pattern = r"\(\d{3}\) \d{3}-\d{4}"

if re.match(pattern, phone_number):
    print("Valid phone number!")
else:
    print("Invalid phone number!")

# ✅ Explanation:
# \(\d{3}\) → Matches (123).
# \d{3}-\d{4} → Matches 456-7890.


# ==============================================================================
# 6. Replacing Spaces with Underscores
# ==============================================================================
text = "Hello World!"
modified_text = re.sub(r"\s", "_", text)
print(modified_text)  # Output: Hello_World!

# ✅ Explanation:
# \s → Matches any whitespace character.
# re.sub(pattern, replacement, text) → Replaces spaces with underscores.


# ==============================================================================
# 7. Extracting a Website URL from Text
# ==============================================================================
text = "Visit our website at https://www.example.com for more info."
url = re.search(r"https?://[a-zA-Z0-9./]+", text)

if url:
    print("Found URL:", url.group())  # Output: https://www.example.com

# ✅ Explanation:
# https?:// → Matches http:// or https:// (the 's' is optional due to ?).
# [a-zA-Z0-9./]+ → Matches the rest of the URL path.


# ==============================================================================
# 8. Splitting a Sentence into Words
# ==============================================================================
text = "apple, banana, cherry"
fruits = re.split(r",\s*", text)  # Splits by commas and optional following spaces
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# ✅ Explanation:
# re.split() → Splits text based on commas and spaces.


# ==============================================================================
# 9. Finding All Numbers in a Sentence
# ==============================================================================
text = "I have 3 apples, 7 bananas, and 12 cherries."
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)  # Output: ['3', '7', '12']

# ✅ Explanation:
# \d+ → Finds all numbers in the text.
# re.findall() → Returns a list of all matches.


# ==============================================================================
# 10. Finding Words That Start with "A" or "a"
# ==============================================================================
text = "Alice and Alex are amazing artists."
words = re.findall(r"\b[Aa]\w+", text)
print("Words found:", words)  # Output: ['Alice', 'Alex', 'amazing', 'artists']

# ✅ Explanation:
# \b → Matches word boundaries (start of a word).
# [Aa] → Matches uppercase or lowercase "A".
# \w+ → Matches the rest of the word.


# ==============================================================================
# 11. Checking if a Password is Strong
# ==============================================================================
# A strong password should have:
# - At least 8 characters
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one number
# - At least one special character
password = "Secure@123"
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

if re.match(pattern, password):
    print("Strong password!")
else:
    print("Weak password! Try adding uppercase, lowercase, numbers, and special characters.")

# ✅ Explanation:
# (?=.*[A-Z]) → Positive lookahead: At least one uppercase letter
# (?=.*[a-z]) → Positive lookahead: At least one lowercase letter
# (?=.*\d) → Positive lookahead: At least one digit
# (?=.*[@$!%*?&]) → Positive lookahead: At least one special character
# [A-Za-z\d@$!%*?&]{8,} → Allowed characters and minimum 8 characters long


# ==============================================================================
# 12. Extracting All Words from a Sentence
# ==============================================================================
text = "Python is fun! Let's learn regex together."
words = re.findall(r"\b\w+\b", text)
print("Words:", words)
# Output: ['Python', 'is', 'fun', 'Let', 's', 'learn', 'regex', 'together']

# ✅ Explanation:
# \b → Word boundary (start and end of a word)
# \w+ → One or more word characters (letters, numbers, underscore)


# ==============================================================================
# 13. Extracting All Email Addresses from a Text
# ==============================================================================
text = "Contact us at support@example.com or sales@company.org."
emails = re.findall(r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\b", text)
print("Emails found:", emails)
# Output: ['support@example.com', 'sales@company.org']

# ✅ Explanation:
# Looks for text matching username@domain.extension format across the whole text.


# ==============================================================================
# 14. Extracting All Hashtags from a Tweet
# ==============================================================================
tweet = "Learning #Python and #Regex is fun! #Coding"
hashtags = re.findall(r"#\w+", tweet)
print("Hashtags found:", hashtags)
# Output: ['#Python', '#Regex', '#Coding']

# ✅ Explanation:
# #\w+ → Finds words starting with '#'.


# ==============================================================================
# 15. Extracting All Capitalized Words (Proper Nouns)
# ==============================================================================
text = "Alice and Bob are learning Python in New York."
capitalized_words = re.findall(r"\b[A-Z][a-z]*\b", text)
print("Capitalized words:", capitalized_words)
# Output: ['Alice', 'Bob', 'Python', 'New', 'York']

# ✅ Explanation:
# \b[A-Z][a-z]*\b → Finds words that start with a capital letter.


# ==============================================================================
# 16. Removing Extra Spaces from a Sentence
# ==============================================================================
text = "Python   is   awesome!"
cleaned_text = re.sub(r"\s+", " ", text)  # Replace multiple spaces with a single space
print(cleaned_text)
# Output: "Python is awesome!"

# ✅ Explanation:
# \s+ → Matches one or more consecutive whitespace characters.


# ==============================================================================
# 17. Extracting All Numbers from a String
# ==============================================================================
text = "I have 3 apples, 10 bananas, and 25 oranges."
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)
# Output: ['3', '10', '25']

# ✅ Explanation:
# \d+ → Finds all consecutive digits.


# ==============================================================================
# 18. Extracting All Words That Start with "T" or "t"
# ==============================================================================
text = "The tiger and the turtle are in the zoo."
words = re.findall(r"\b[Tt]\w+", text)
print("Words found:", words)
# Output: ['The', 'tiger', 'the', 'turtle', 'the']

# ✅ Explanation:
# \b[Tt]\w+ → Finds words that start with 'T' or 't'.


# ==============================================================================
# 19. Checking if a String Contains Only Letters and Numbers
# ==============================================================================
text = "Python123"
if re.fullmatch(r"[A-Za-z0-9]+", text):
    print("Valid input (letters and numbers only)")
else:
    print("Invalid input!")

# ✅ Explanation:
# re.fullmatch() → Checks if the entire string matches the pattern from start to end.
# [A-Za-z0-9]+ → Allows only alphanumeric characters.