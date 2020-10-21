"""Python functions for JavaScript Trials 1."""
def output_all_items(items):
    # TODO: replace this line with your code
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
      # TODO: replace this line with your code
    results = []

    for i in range(len(items)):
        if i % 2 != 0:
            results.append(items[i])
    return results


def print_as_numbered_list(items):
    for i in range(len(items)):
        print(f"{i + 1}. {items[i]}")


def get_range(start, stop):
     # TODO: replace this line with your code
    nums =[]
    for num in (range(start, stop)):
        nums.append(num)
    return nums
    

def censor_vowels(word):
    chars = []
    vowels = ["a", "e", "i", "o", "u"]
    # letter = word.split()
    # print(letter)

    for char in word:
        if char in vowels:
            # print(char)
            char = "*"
        chars.append(char)
    
    return "".join(chars)


def snake_to_camel(string):
     # TODO: replace this line with your code
    camel_case = []
    for word in string.split("_"):
        camel_case.append(f"{word[0].upper()}{word[1:]}")
    return "".join(camel_case)


def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if longest < len(word):
            longest = word
    return longest

def truncate(string):

    result = []
    for char in string:
        if (len(result) == 0) or (char != result[len(result)-1]):
            result.append(char)
    return ''.join(result) 



def has_balanced_parens(string):
    
    parens = 0
    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
            if (parens > 0):
                return False
    return parens < 0

def compress(string):
    compressed = []
    curr_char = ''
    charcount = 0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            if charcount > 1:
                compressed.append(str(charcount))
            curr_char = char
            charcount = 0   
        charcount += 1
    compressed.append(curr_char)
    if charcount >1:
        compressed.append(str(charcount))
    return ''.join(compressed)



