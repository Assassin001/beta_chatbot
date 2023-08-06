import time

def time_1():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    response = "Current time is: " + current_time
    return response

def greet_user():
    response = "Hello! How can I assist you today?"
    return response

def farewell_user():
    response = "Goodbye! Have a great day!"
    return response
