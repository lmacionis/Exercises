"""
Assign to a variable in your program a triple-quoted string that contains your
favourite paragraph of text — perhaps a poem, a speech, instructions to bake a
cake, some inspirational verses, etc.

Write a function which removes all punctuation from the string, breaks the
string into a list of words, and counts the number of words in your text
that contain the letter “e”. Your program should print an analysis of the text like this:

Your text contains 243 words, of which 109 (44.8%) contain an "e".
"""

#FOUND THE MAIN FUNCTION IN THE STACKOWERFLOW.COM, JUST REMAID IT BY MY CONDITIONS.
def count(text):
    punctuations = ".,?!"

    numberOfe = 0
    total_words = 0
    # REMOVING ALL PUNCTUATIONS, BUT I DONT REALY NEED THAT FOR THE CORECT ANSWER
    for x in text.lower():
        if x in punctuations:
            text = text.replace(x, "")
    # BREAKING A STRING INTO A LIST CANT MAKE IT, AND DONT UNDERSTAND WHY I NEED THAT

    # COUNTING THE NUMBER OF WORDS AND LETTERS E IN THE STRING
    for word in text:
        if word in text:
            total_words = len(text.split())
            if word == 'e':
                numberOfe = numberOfe + 1


    percent_with_e = (numberOfe/total_words) * 100
    print(text)         # PRINTING THE STRING WITHOUT THE PUNCTUATIONS, JUST FOR CHECK IN.
    print("Your text contains", total_words, "words, of which", numberOfe, "(", percent_with_e, "%)", "contain an 'e'.")


text = '''"Nature loves courage. Whats the payoff on that? It shows you that it loves courage,
becouse it will remove obsticles. You make the commitment and nature will responde to that
commitment by removing imposible obsticles. Dream the imposible dream and
the world will not graind you under, it will lift you up."'''

count(text)