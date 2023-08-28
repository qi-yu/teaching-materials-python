word_dict = {"black": "adj",
             "computer": "noun",
             "sunny": "adj",
             "sleep": "verb"}

def get_words(word_class):
    for k, v in word_dict.items():
        if v == word_class:
            print(k)

print("ALL ADJECTIVES:")
get_words("adj")
print()

print("ALL NOUNS:")
get_words("noun")
print()