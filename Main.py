from Scheme import Scheme
import time


if __name__ == "__main__":
    scheme = Scheme()

    scheme.print()
    while not scheme.is_completed() and scheme.get_winner() == 0:
        move = input('Make your move. (0 = -, 1 = x, 2 = o)\n')
        scheme.set(move.split())
        scheme.print()

        if not scheme.is_completed() and scheme.get_winner() == 0:
            time.sleep(1)
            print('Computer move')
            scheme.add_random(2)
            scheme.print()

    print("The winner is: " + str(scheme.get_winner()))
