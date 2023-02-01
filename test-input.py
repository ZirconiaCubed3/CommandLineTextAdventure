from blessed import Terminal
import asyncio
import time

term = Terminal()
currentIn = ""

async def inputReader():
  with term.cbreak():
    return term.inkey()

async def main():
  global currentIn
  currentIn = await inputReader()

asyncio.run(main())
while True:
  print("hello")
  time.sleep(1)
  if currentIn:
    print(currentIn)
    currentIn = ""
