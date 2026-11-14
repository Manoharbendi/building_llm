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

# now calculating the probability
pair_prods={}

for current_word in pair_count:
    pair_prods[current_word]={}
    total=sum(pair_count[current_word].values())

    for next_word in pair_count[current_word]:
        pair_prods[current_word][next_word]=pair_count[current_word][next_word]/total
        
# print("\nprobabilty after the:")
# for word, prob in sorted(pair_prods["the"].items(), key=lambda x: -x[-1]):
#     print(f"{word}: {prob:.1%}")

# probabilty after the:
# king: 37.0%
# queen: 25.9%
# people: 11.1%
# garden: 7.4%
# palace: 7.4%
# kingdom: 7.4%
# beautiful: 3.7

import random
def generating_token(start_word,num_word=20):
    current_word=start_word
    output=[current_word]

    for _ in range (num_word):
        # dead end - this was not follwed by anything 
        if current_word not in pair_prods:
            break
        # get there options and there probabilities
        option =list(pair_prods[current_word].keys())
        probabilities=list(pair_prods[current_word].values())

        # sampling the responce from the distrutions
        next_word= random.choices(option, weights=probabilities,k=1)[0]

        output.append(next_word)
        current_word=next_word
    return " ".join(output)

print("text gererated by the Bigram Model:")
for i in range(5):
    print(f"{i+1} {generating_token('the',5)}")