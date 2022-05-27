# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from sqlalchemy import false


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if "".join(reversed(word))== anagram:
        return True
    else:
        return False
    
    
print(find_anagram("book", "kob"))
word = "helloworld"
print(word.lstrip(" "))
print("".join("hih"))

