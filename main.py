print("Welcome to GC mini golf!")
myName = input("What is your name?")
score_sum = 0
response = input(f"Hi, {myName}! Would you like to play 3 or 6 holes?")
response = int(response)
for i in range(response):
    putts = int(input(f"How many putts for Hole {i+1}? (par 3)"))
    score_sum += putts

score = score_sum - response * 3

message = ""

plus_symbol = ""

if score > 0:
  message = "Nice Try"
  plus_symbol = "+"
elif score == 0:
  message = "Good game"
elif score < 0:
  message = "Great job"

print(f"{message}, {myName}. Your score was {plus_symbol}{score}.")
