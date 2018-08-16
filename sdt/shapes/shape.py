class Shape:

    """ This is a shape base class.
    all subclasses have to override draw method to create new shapes.
    """

    _type = None

    def draw(self):
        pass

    def getType(self):
        return self._type
