class TileMap():
  def __init__(self, size, map, landSymbol="l", waterSymbol="w", doorSymbol="d", grassSymbol="g"):
    self.sizeX = size[0]
    self.sizeY = size[1]
    self.l = landSymbol
    self.w = waterSymbol
    self.d = doorSymbol
    self.g = grassSymbol
    self.map = map
