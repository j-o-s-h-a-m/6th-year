# Question 16 (a)
# Examination Number:

# Function to calculate readability score of text
def calculate_readability_score(text):

# Split the text into a list of words
    words = text.split()
    print("\nThe list of words in the text is:\n", words)

# Initialise the word counters
    word_count = len(words) # Number of words in list
    short_word_count = 0
    count = 0
    for i in words:
        if len(i) <= 2:
            short_word_count += 1
#         for j in i:
#             count += 1
#         if count <= 2:
#             short_word_count += 1
#         count = 0
    print(short_word_count)
            

    # Initialise the number of sentences
    sentence_count = text.count(".")

    # Calculate the readability score
    score = (0.4)*((word_count/sentence_count) + 100 * ((word_count - short_word_count)/(word_count)))
    score = round(score, 2) # Round the score to 2 d.p.

    return score, short_word_count 

# Set the text for analysis
text1 = "Elaborate sentences influence readability in subtle and unpredictable ways."
text2 = "I do not like green eggs and ham! I do not like them Sam I am!"

# Calculate the score for text1
score1 = calculate_readability_score(text1)
print('Readability Score 1:', score1,'\n')

#calculate the score for text2
score2 = calculate_readability_score(text2)
print('readability Score 2:', score2,'\n')


if score1 < score2:
    print('The first text is easier to read.')
elif score1 > score2:
    print('The second text is easier to read')
else:
    print('both score are the same')
    
