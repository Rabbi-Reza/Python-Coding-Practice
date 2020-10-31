
# def capitalizeWord(words):
#
#     if len(words) == 1:
#         return words[0].upper()
#     else:
#         capitalizeWord(words[1:])
#         return words[0].upper()

def capitalizeWords(arr):
    result = []

    if len(arr) == 0:
        return result

    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])

words =['i','am','learning','coding']

# print(words[2])
# word = words[2]
# print(word)

print(capitalizeWords(words))