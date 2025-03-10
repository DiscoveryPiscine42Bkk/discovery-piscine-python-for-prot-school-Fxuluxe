def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

# Call the greetings function with different arguments
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)