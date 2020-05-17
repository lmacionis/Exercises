"""
Count how many words in a list have length 5.
"""

list = ["sex", "arabica", "Lukas", "Rex", "kavos", "words"]

def words_in_list(words):
    count_words = 0
    for i in words:
        if len(i) == 5:
            count_words = count_words + 1
    return count_words


print(words_in_list(list))