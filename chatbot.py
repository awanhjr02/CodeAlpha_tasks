# Importing necessary libraries
import spacy     # spaCy is used for natural language processing (NLP)
import random  

# Loading the small English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# Defining a dictionary with various types of responses.
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
    elif any(token.lemma_ in ["bye", "goodbye", "see you"] for token in doc):
        return "bye"
    elif any(token.lemma_ in ["thank", "thanks"] for token in doc):
        return "thank"
    else:
        return "default"

# Function to select a random response based on the detected intent
def get_response(intent):
    return random.choice(responses[intent])

# Main function that controls the conversation with the user
def chatbot():

    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye!")
            break  
        
        intent = get_intent(user_input)
        
        response = get_response(intent)
        
        print(f"Chatbot: {response}")

# If this script is being run directly ( not imported as a module), start the chatbot
if __name__ == "__main__":
    chatbot()
