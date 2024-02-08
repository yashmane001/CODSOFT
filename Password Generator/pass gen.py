import random
import string
import math


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def calculate_crack_time(password):
    # Number of possible characters
    possible_characters = 94  # 26 lowercase letters + 26 uppercase letters + 10 digits + 32 special characters

    # Calculate the number of possible combinations
    combinations = possible_characters ** len(password)

    # Estimate the time to crack based on an assumption of 10 billion guesses per second
    seconds_to_crack = combinations / 10e9

    # Convert seconds to more readable format
    time_to_crack = convert_seconds(seconds_to_crack)

    return time_to_crack


def convert_seconds(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.2f} minutes"
    elif seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.2f} hours"
    else:
        days = seconds / 86400
        return f"{days:.2f} days"


def main():
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    print("Generated Password:", password)
    crack_time = calculate_crack_time(password)
    print("Time to crack:", crack_time)


if __name__ == "__main__":
    main()
