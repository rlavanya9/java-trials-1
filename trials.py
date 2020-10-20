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
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
