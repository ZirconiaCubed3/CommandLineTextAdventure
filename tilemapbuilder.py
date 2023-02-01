from utils import printGrid, saveTileMap
import random

sizeX = int(input("Size of X Axis? "))
sizeY = int(input("Size of Y Axis? "))
options = ["land", "water", "grass"]
map = [["0" for i in range(sizeX)] for j in range(sizeY)]
for x in range(sizeX):
  for y in range(sizeY):
    map[y][x] = "1"
#    printGrid(map, wrapper=" ")
#    cell = input("Tile type for (%s, %s)? " % (y, x))
    cell = random.choice(options)
    map[y][x] = {"type": cell.lower()}
printGrid(map, wrapper=" ")
name = input("Name of TileMap? ")
saveTileMap(name, map)
