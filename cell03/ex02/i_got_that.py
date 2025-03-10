def main():
    
    while True:
        
        user_input = input("Enter something (or type 'STOP' to quit): ")
        
        if user_input.upper() == "STOP":
            print("You stopped the program. Goodbye!")
            break
        
        print(f"I got that: {user_input}")

if __name__ == "__main__":
    main()
