import random

def randomquote(quotes):
  last = len(quotes) -1
  rnd = random.randint(0,last)
  print("Random Quote: ",quotes[rnd])


f = open("quotes.txt")
quotes = f.readlines()
f.close()

selection = "A"

while True:
  selection = input("(D)isplay a quote\n(A)dd a quote\nChoose your selection by typing in the letter: ")
  if selection.upper() == "D":
    randomquote(quotes)
  elif selection.upper() == "A":
    quotetoadd = input("What saying would you like to add to the file?: ")
    filewritingto = open("quotes.txt",'a')
    filewritingto.write(quotetoadd + "\n")
    filewritingto.close()
    print("'",quotetoadd,"' has been written to the file!")
  else:
    print("Exiting...")
    break


