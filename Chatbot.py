print("Hello! I am AI BOT! What's your name?")
name=input()
print(f"Nice to meet you {name}!")
print("How are you feeling today? (good/bad)")
feeling=input().lower()
if feeling=="good":
    print("I'm glad to hear that!")
elif feeling=="bad":
    print("I'm sorry to hear that! I hope things get better soon!")
else:
    print("I see. Sometimes it is hard to put feelings into words.")
print(f"It was nice chatting with you {name}! Goodbye!")