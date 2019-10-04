class Probe:
    """Probe implementation
    Usage::
        >>> from probe import Probe
        >>> probe = Probe(5, 5, 0, 0, "N")
        >>> proble.explore("LMMLMLMRMLLM")
        >>> print(probe)
    :param map_h: map length
    :param map_w: map width
    :param init_x: horizontal initial position
    :param init_y: lenght initial position
    :param init_d: initial probe orientation
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
        self.directions = {
            90: "N", 
            270: "S", 
            0: "E", 
            180: "W"
        }

        self.degrees = {
            "N": 90, 
            "S": 270, 
            "E": 0, 
            "W": 180
        }

        self.cur_degree = self.degrees.get(init_d)

    def __str__(self):
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
