def shout(text):
    returntext.upper()
def whisper(text):
    returntext.lower()


#yell=shout

#New variable for the function

def person_does(name,func):
    return name +"says"+func("How has your day been?")

#message=shout("Hello how are you?")
#print(message)

message=person_does("nico", shout)
print(message)
message=person_does("nico", whisper)
print(message)