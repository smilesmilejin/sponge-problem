
# Method 1
# def sponge_case(sentence):
#     # Write your solution here!
#     # pass

#     sentence_list = sentence.split(" ")

#     result = []
#     for word in sentence_list:
#         result.append(sponge_word(word))

#     return " ".join(result)


# def sponge_word(word):
#     for i in range(len(word)):
#         if i % 2 == 0:
#             word = word[:i] + word[i].lower() + word[i+1:]
#         else:
#             word = word[:i] + word[i].upper() + word[i+1:]
    
#     return word


# Method 2
def sponge_case(sentence):
    # Write your solution here!
    # pass

    i = 0
    while i < len(sentence):
        if i == 0:
            sentence = sentence[i].lower() + sentence[i+1:]
            i += 1
            continue
        if sentence[i] == " ":
            sentence = sentence[:i+1] + sentence[i+1].lower() + sentence[i+2:]
            i += 2
            continue

        if sentence[i-1].islower():
            sentence = sentence[:i] + sentence[i].upper() + sentence[i+1:]
            i += 1
        elif sentence[i-1].isupper():
            sentence = sentence[:i] + sentence[i].lower() + sentence[i+1:]
            i += 1
        
    return sentence



# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")