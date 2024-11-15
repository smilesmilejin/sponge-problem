def sponge_case(sentence):
    # turn the sentence into an array of individual words
    words = sentence.split()

    # create a new array of sponge-case words using our helper function
    new_words = []
    for word in words:
        new_words.append(sponge_single_word(word))

    # Join the new spongy words with spaces
    return " ".join(new_words)


# Helper function that converts a single word to sponge-case 
def sponge_single_word(word):
    new_word = ""
    # Instructions say the word must start with a lowercase letter
    # We will toggle this variable to alternate between lower and upper case
    lower = True 

    for letter in word:
    # if our toggle is set to lowercase, add a lowercase version of the letter
        if lower:
            new_word += letter.lower()
        # if our toggle is set to lowercase, add a uppercase version of the letter
        else:
            new_word += letter.upper()
        # flip our toggle
        lower = not lower
    
    return new_word



# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")

"""
***NOTES TO INTERVIEWER***

---------Answers to clarifying questions----------
Q: What should I do if the input is not a string? Or if the string is empty?
A: You do not need to worry about this case. You can assume the input will be a string with at least one letter in it.

Q: What should I do with punctuation, numbers, etc.?
A: You can assume the input will include only letters and spaces.

Q: What should I do if there's extra spaces?
A: You can assume there will be exactly one space in between words and no extra spaces at the beginning or end of the string.

--------------------------------------------------



---------Hints if needed----------

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and desrcibe how they would do it using only pen and paper

- If they're having trouble determining how to handle multiple words, encourage them to first write code to solve the case where there's only a single word in the string

- If your candidate is struggling to determine how to convert a letter to upper or lower case, encourage them to look up how to do that online

- If your candidate is struggling with test case #3, remind them that the question states that every word starts with a lowercase letter

-------------------------------------------------

"""