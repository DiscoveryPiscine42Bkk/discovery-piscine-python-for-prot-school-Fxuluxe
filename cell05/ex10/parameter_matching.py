import sys

def parameter_matching():
    if len(sys.argv) != 2:
        print("none")
        return
  
    expected_word = sys.argv[1]
   
    user_input = input("Enter a word: ")
   
    if user_input == expected_word:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    parameter_matching()
