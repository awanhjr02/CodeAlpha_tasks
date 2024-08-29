# Importing necessary libraries
import spacy  # spaCy is used for natural language processing (NLP)
import random  # random is used to select a random response from a list

# Loading the small English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# Defining a dictionary with various types of responses.
# The keys represent intents (like 'greet', 'bye', 'thank', 'default'),
# and the values are lists of responses that the chatbot can give.
responses = {
    "greet": [
        "Hello! How can I assist you today?", 
        "Hi there! What can I do for you?", 
        "Hello! How's it going?"
    ],
    "bye": [
        "Goodbye! Have a great day!", 
        "See you later!", 
        "Bye! Take care!"
    ],
    "thank": [
        "You're welcome!", 
        "No problem!", 
        "Glad I could help!"
    ],
    "default": [
        "I'm sorry, I didn't understand that.", 
        "Can you please rephrase?", 
        "I'm not sure what you mean."
    ]
}

# Function to determine the user's intent based on their input
def get_intent(text):
    # Process the user's input using spaCy to analyze the text
    doc = nlp(text.lower())
    
    # Check if the user's input contains words that indicate a greeting
    if any(token.lemma_ in ["hello", "hi", "hey"] for token in doc):
        return "greet"
    # Check if the user's input contains words that indicate they want to say goodbye
    elif any(token.lemma_ in ["bye", "goodbye", "see you"] for token in doc):
        return "bye"
    # Check if the user's input contains words that indicate they are thanking the chatbot
    elif any(token.lemma_ in ["thank", "thanks"] for token in doc):
        return "thank"
    # If none of the above conditions are met, return "default"
    else:
        return "default"

# Function to select a random response based on the detected intent
def get_response(intent):
    # Select a random response from the list of responses for the given intent
    return random.choice(responses[intent])

# Main function that controls the conversation with the user
def chatbot():
    # Print a greeting to the user when the chatbot starts
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    
    # Start a loop that continues the conversation until the user decides to exit
    while True:
        # Get input from the user
        user_input = input("You: ")
        
        # If the user types 'bye', 'exit', or 'quit', end the conversation
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye!")
            break  # Break the loop to end the program
        
        # Determine the intent of the user's input
        intent = get_intent(user_input)
        
        # Get a response based on the detected intent
        response = get_response(intent)
        
        # Print the chatbot's response
        print(f"Chatbot: {response}")

# If this script is being run directly (and not imported as a module), start the chatbot
if __name__ == "__main__":
    chatbot()
