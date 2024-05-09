import random as rd

def greet_customer():

  greet = rd.choice(["Hello! Welcome to our customer service chat. ",
                    "Good morning !",
                    "Welcome to Chatbot !"])
  print(greet)
  # print("Hello! Welcome to our customer service chat. ")
  # print("I'm here to answer your questions or help you with your requests.")

def get_customer_query():

  while True:
    query = input("How can I help you today? ")
    
    if query:  # Query must be non-empty
      return query.lower()  # Convert input to lowercase for easier comparison
    else:
      print("Please enter a question or request.")

def respond_to_query(query):
  # Response to these keywords
  
  greetings = ["hi", "hello", "hey"]
  thanks = ["thank you", "thanks"]
  order_related = ["order", "shipment", "delivery", "track"]
  return_related = ["return", "refund"]
  support_related = ["help", "support"]
  
  #Responses
  if any(word in query for word in greetings):
    return "Hi there! How can I assist you today?"
  elif any(word in query for word in thanks):
    return "You're welcome! Glad I could help."
  elif any(word in query for word in order_related):
    return "For order inquiries, please provide your order number for further assistance."
  elif any(word in query for word in return_related):
    return "For return and refund information, please visit our returns policy page at [link to return policy]."  
  elif any(word in query for word in support_related):
    return "For further assistance, please contact our customer support team at [phone number] or [email address]."  
  else:
    return "I apologize, I can't answer that question yet. However, I'm still under development and learning. Perhaps you can rephrase your question?"

def main():
  
  
  while True:
    engine = input("'start' or 'stop' :-")
    if engine == "start":
      greet_customer()
      query = get_customer_query()
      response = respond_to_query(query)
      print(response)
    elif engine == "stop":
      print("Engine stopped ! ")
      break
    else :
      print("Please enter a valid input")
      

if __name__ == "__main__":
  main()
