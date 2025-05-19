def sponge_case(sentence):
    # Write your solution here!
    # pass

    sentence_list = sentence.split(" ")

    reformated_sentence_list = []
    for word in sentence_list:
        # print(sponse_word(word))
        reformated_sentence_list.append(sponse_word(word))

    # print(reformated_sentence_list)
    # print("".join(reformated_sentence_list))
    return " ".join(reformated_sentence_list)


def sponse_word(sentence):
    for i in range(len(sentence)):
        if i == 0:
            sentence = sentence[i].lower() + sentence[i+1:]
            continue
        if sentence[i-1].islower():
            sentence = sentence[:i] + sentence[i].upper() + sentence[i+1:]
        elif sentence[i-1].isupper():
            sentence = sentence[:i] + sentence[i].lower() + sentence[i+1:]

    return sentence


# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")