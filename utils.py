def wrap(char, wrapper):
  if wrapper == None:
    return str(char)
  else:
    return str(wrapper) + str(char) + str(wrapper)

def colorString(char, color):
  prefix = "\u001b["
  escape = prefix + "0m"
  if color.lower() == "black":
    return prefix + "30m" + str(char) + escape
  elif color.lower() == "red":
    return prefix + "31m" + str(char) + escape
  elif color.lower() == "green":
    return prefix + "32m" + str(char) + escape
  elif color.lower() == "yellow":
    return prefix + "33m" + str(char) + escape
  elif color.lower() == "blue":
    return prefix + "34m" + str(char) + escape
  elif color.lower() == "magenta":
    return prefix + "35m" + str(char) + escape
  elif color.lower() == "cyan":
    return prefix + "36m" + str(char) + escape
  elif color.lower() == "white":
    return prefix + "37m" + str(char) + escape

def printGrid(grid, wrapper=None):
  xLen = len(grid[0])
  for line in grid:
    for i, e in enumerate(line):
      if (i + 1) % xLen != 0:
        if wrapper:
          print(wrap(e, wrapper), end='')
        else:
          print(e, end='')
      else:
        if wrapper:
          print(wrap(e, wrapper))
        else:
          print(e)

def showTileMap(tilemap, playerSymbol="o", playerPos=[0, 0], showPlayer=False, wrapper=" "):
  newMap = []
  for x in range(len(tilemap.map[0])):
    newMap.append([])
    for y in range(len(tilemap.map)):
      for z in range(2):
        if showPlayer and playerPos == [x, y]:
          newMap[x].append(wrap(playerSymbol, wrapper))
        elif tilemap.map[y][x]["type"] == "land":
          newMap[x].append(wrap(colorString(tilemap.l, "yellow"), wrapper))
          newMap[x].append(wrap(colorString(tilemap.l, "yellow"), wrapper))
        elif tilemap.map[y][x]["type"] == "water":
          newMap[x].append(wrap(colorString(tilemap.w, "blue"), wrapper))
          newMap[x].append(wrap(colorString(tilemap.w, "blue"), wrapper))
        elif tilemap.map[y][x]["type"] == "grass":
          newMap[x].append(wrap(colorString(tilemap.g, "green"), wrapper))
          newMap[x].append(wrap(colorString(tilemap.g, "green"), wrapper))
        elif tilemap.map[y][x]["type"] == "door":
          newMap[x].append(wrap(colorString(tilemap.d, "black"), wrapper))
          newMap[x].append(wrap(colorString(tilemap.d, "black"), wrapper))
        else:
          newMap[x].append(".")
          newMap[x].append(".")
  printGrid(newMap)

def loadTileMap(name):
  return eval(open("./maps/" + name + ".map", "r").read())

def saveTileMap(name, map):
  with open("./maps/" + name + ".map", "w") as file:
    file.write(str(map))
