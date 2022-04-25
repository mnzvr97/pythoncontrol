# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:
def phrase(): 
    prompt = input("please enter a word or phrase:")
# 2. Print the following message:
#      - What you entered is xx characters long
    length = len(prompt)
    print(f"what you entered is {length} characters long")
    
# 3. Return to step 1, unless the word 'quit' was entered.
    if prompt != "quit":
        phrase()
phrase()
