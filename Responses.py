from datetime import date, datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ("hello", "hi", "hey", "sup",):
        return "Hey! How's it going?"
    
    if user_message in ("who are you", "who are you?", "who you"):
        return "I am Every Mind Matters bot. I am here to help you as much as I can. Let me know what you want me to help you with. :)"
    
    if user_message in ("help", "please help", "i want help"):
        return "I am Every Mind Matters bot. I am here to help you as much as I can. Let me know what you want me to help you with. :)"
    
    
    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y. %H:%M:%S")
        
        return str(date_time)
    
    return "I am sorry. I don't understand you :("
    