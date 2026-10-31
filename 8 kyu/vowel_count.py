# =================================================
# Instruction
# =================================================

# # Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# =================================================
# Solution
# =================================================

def get_count(sentence):
    count = 0
    for x in sentence:
        if x in 'aeiou':
            count += 1


# alternative solution using list comprehension
def get_count(sentence):
    return sum(1 for x in sentence if x in 'aeiou')

