class Probe:
    """Probe implementation
    Usage::
        >>> import game
        >>> game = Game(20, 20, [(2,1), (0, 1), (0, 2)])
        >>> print(game)
        >>> game.next_generation()
        >>> print(game)
    :param init_x: number of columns
    :param init_y: number of rows
    :param init_d: initial cells population
    """
    
    def __init__(self, map_h=0, map_w=0, init_x=0, init_y=0, init_d="N"):
        self.map_h = int(map_h)
        self.map_w = int(map_w)
        self.init_x = int(init_x)
        self.init_y = int(init_y)
        self.init_d = init_d
        self.cur_x = int(init_x)
        self.cur_y = int(init_y)
        self.cur_d = init_d
        self.cur_degree = 0
        self.directions = {
            90: "N", 
            270: "S", 
            0: "L", 
            180: "W"
        }

    def __str__(self):
        print "%s %s %s" % (self.cur_x, self.cur_y, self.cur_d)
        return str("%s %s %s" % (self.cur_x, self.cur_y, self.cur_d))

    def explore(self, instructions):
        """Explore all terrain"""

        for instruct in instructions:
            if instruct is "L":
                self.__spin_L()
            elif instruct is "R":
                self.__spin_R()
            elif instruct is "M":
                self.__move()

    def __move(self):
        # Direction to N
        if self.cur_d == "N":
            if self.cur_y < self.map_h:
                self.cur_y = self.cur_y + 1
        # Direction to S
        if self.cur_d == "S":
            if self.cur_y > 0:
                self.cur_y = self.cur_y - 1
        # Direction to E
        if self.cur_d == "E":
            if self.cur_x < self.map_w:
                self.cur_x = self.cur_x + 1
        # Direction to W
        if self.cur_d == "W":
            if self.cur_x > 0:
                self.cur_x = self.cur_x - 1

    def __spin_R(self):
        degree = self.__set_degree("R")
        self.cur_d = self.directions.get(degree)

    def __spin_L(self):
        degree = self.__set_degree("L")
        self.cur_d = self.directions.get(degree)
    
    def __set_degree(self, orientation):
        if orientation is "R":
            if self.cur_degree == 0:
                self.cur_degree = 270
            else:
                self.cur_degree = self.cur_degree - 90
                
        if orientation is "L":
            if self.cur_degree == 270:
                self.cur_degree = 0
            else:
                self.cur_degree = self.cur_degree + 90

        return self.cur_degree
