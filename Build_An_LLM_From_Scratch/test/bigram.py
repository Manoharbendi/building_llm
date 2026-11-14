text = """
the king loved the queen and the queen loved the king
the king loved playing cricket in the garden
the queen loved playing chess in the palace
the king and the queen walked in the garden
the king loved the kingdom and the people loved the king
the queen visited the king in the palace
the king played cricket with the people
the queen loved the beautiful garden
the king and queen ruled the kingdom
the people loved the king and the queen
"""

print(text)
word=text.lower().split()
print(word)

# print(f"the length of the word list is: {len(word)}")
# print(f"first ten words:{word[:10]}")

pair_count={}

for i in range(len(word) - 1):
    current_word = word[i]
    next_word = word[i + 1]

    if current_word not in pair_count:
        pair_count[current_word] = {}

    pair_count[current_word][next_word] = pair_count[current_word].get(next_word, 0) + 1

print ("after 'the'",pair_count["the"])
print ("after 'king'",pair_count["king"])
print ("after 'queen'",pair_count["queen"])
print ("after 'garden'",pair_count["garden"])

