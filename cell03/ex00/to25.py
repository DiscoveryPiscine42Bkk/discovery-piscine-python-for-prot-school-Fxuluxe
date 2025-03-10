def main():
    
    num = float(input("Enter a number: "))
    
    
    if num > 25:
        print("Error")
    else:
        
        while num <= 25:
            print(int(num)) 
            num += 1 

if __name__ == "__main__":
    main()
