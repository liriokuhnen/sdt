from sdt.shapes.types.triangle import Triangle


class ShapeFactory:

    """ Manage shapes.
    Factory, that encapsulates shape initialization and then allows instatiation
    of the classes to draw Shapes.
    """

    __triangle = None

    @staticmethod
    def initialize():
        ShapeFactory.__triangle = Triangle()

    @staticmethod
    def drawTriangle(a, b, c):
        return ShapeFactory.__triangle.draw(a, b, c)
