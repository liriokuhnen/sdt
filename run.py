import readline
from sdt.shapes.shape_factory import ShapeFactory

ShapeFactory.initialize()


def main():
    running = True

    print('Hello, I am a smart robot who will help you check the type of a triangle')

    while running:
        try:
            a = input('Please inform a number to value A:')
            b = input('Please inform a number to value B:')
            c = input('Please inform a number to value C:')

            triangle_type = ShapeFactory.drawTriangle(int(a),
                                                      int(b),
                                                      int(c)).getType()
            print("### RESULT ### - {}".format(triangle_type))
        except Exception:
            print("### ERROR ### - please just inform numbers")
        except KeyboardInterrupt:
            running = False
            print('\nBye bye')

if __name__ == "__main__":
    main()
