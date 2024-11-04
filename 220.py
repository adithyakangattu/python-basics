#Write a Python function called greet_friends

# that can take an arbitrary number of friend names as arguments.
# The function should print a greeting for each friend
# in the format: "Hello, [friend_name]!".
# If no names are provided,
# the function should print: "No friends to greet."
# Call the function with the names "Alice", "Bob", and "Charlie".


def greet_friends(*friendsnames):
    if not friendsnames:
        print("no friends to greet.")
    else:
        for friend in friendsnames:
            print(f"hello , {friend}!")

greet_friends("adhi","aaru","chandu")