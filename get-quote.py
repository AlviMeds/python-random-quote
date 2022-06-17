import random
def primary():
   print("Keep it logically awesome.")

f = open("D:\Python\python-random-quote\get-quote.py")
quotes = f.readlines()
f.close()

last = 13
rnd = random.randint(0, last)
print(quotes[rnd])



if __name__== "__main__":
  primary()
