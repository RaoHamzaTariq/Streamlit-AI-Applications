import random
import string

def generate_strong_password():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*"

    # Ensure the password meets all criteria
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password with random choices from all sets
    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=4)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)