number_of_words = int(input())
words = []
unique_words = []

for i in range(number_of_words):
    new_word = input()
    words.append(new_word)
    if new_word not in unique_words:
        unique_words.append(new_word)

print(len(unique_words))
for unique_word in unique_words:
    print(words.count(unique_word), end=" ")