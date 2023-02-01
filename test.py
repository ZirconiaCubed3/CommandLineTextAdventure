from tilemap import TileMap
from utils import loadTileMap, printGrid, showTileMap
import time
import threading
import os
import sys
from blessed import Terminal
import platform

if platform.system() == "Windows":
  CLEAR = "cls"
else:
  CLEAR = "clear"

term = Terminal()

map = loadTileMap("randomTileMap1")
tilemap = TileMap([4, 4], map, landSymbol="#", waterSymbol="#", doorSymbol="#", grassSymbol="#")
playerPos = [0, 0]
running = True
while running:
  os.system(CLEAR)
  showTileMap(tilemap, showPlayer=True, playerPos=playerPos, wrapper=None)
  with term.cbreak():
    command = term.inkey()
  if "exit" in command:
    running = False
  elif "\033[D" in command:
#    Left Arrow
    try:
      if tilemap.map[playerPos[1]-1][playerPos[0]]["type"] != "water":
        playerPos[1] -= 1
    except Exception as e:
      pass
  elif "\033[A" in command:
#    Up Arrow
    try:
      if tilemap.map[playerPos[1]][playerPos[0]-1]["type"] != "water":
        playerPos[0] -= 1
    except Exception as e:
      pass
  elif "\033[B" in command:
#    Down Arrow
    try:
      if tilemap.map[playerPos[1]][playerPos[0]+1]["type"] != "water":
        playerPos[0] += 1
    except Exception as e:
      pass
  elif "\033[C" in command:
#    Right Arrow
    try:
      if tilemap.map[playerPos[1]+1][playerPos[0]]["type"] != "water":
        playerPos[1] += 1
    except Exception as e:
      pass
  elif "\t" in command:
#    Tab Key
    running = False
  command = ""
