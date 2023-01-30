print("~~ PALINDROME TEST ~~")
print()

# function definition
while True:
  def isPalindrome (s):
    s = ''.join(e for e in s if e.isalnum()) #ignore spaces and punctuation
    s = s.lower() #ignore case sensitivity
    return s == s[::-1]
    
# exit command
  s=input("Enter string to test for Palindrome or hit 'exit': ")
  if s == "exit":
    break

#calls function
  ans = isPalindrome(s)
  print(ans)

# exit screen
print("Have a nice day!")

