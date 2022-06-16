# https://www.codewars.com/kata/53f40dff5f9d31b813000774

def recoverSecret(triplets, *args):
    def all_equal(iterator):
        iterator = iter(iterator)
        first = next(iterator)
        return all(first == x for x in iterator)

    dict_letter = {}
    current_triplets = []

    for triplet in triplets:
        for letter in triplet:
            if letter not in dict_letter.keys():
                dict_letter[letter] = []
            if triplet.index(letter) != len(triplet) - 1:
                dict_letter[letter].append(triplet[triplet.index(letter) + 1:])
    index_last_letter = list(dict_letter.values()).index([])
    last_letter = list(dict_letter.keys())[index_last_letter]
    for x in triplets:
        current_triplets.append([i for i in x if i != last_letter])
    if args != ():
        last_letter += args[0]
    if all_equal(current_triplets):
        return last_letter[::1]
    return recoverSecret(current_triplets, last_letter)
