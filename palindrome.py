def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def main():
    user = input("Enter a word ")
    check = palindrome(user)
    if check == True:
        print("You've got a palindrome!")
    else:
        print("No palindrome here")

main()
