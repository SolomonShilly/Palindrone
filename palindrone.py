def is_palindrone(string):
    reverseString = string[::-1]
    return string == reverseString

word = 'madam'
if is_palindrone(word):
  print(f"{word} is a palindrone")
else:
  print(f"{word} is not a palindrone")
