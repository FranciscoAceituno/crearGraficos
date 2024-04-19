import sys
import time


class Funciones:
    def make_it_flash(self, text):
        for i in reversed(range(6)):
            sys.stdout.write('\r')
            sys.stdout.write(text if i % 2 else ' '*len(text))
            sys.stdout.flush()
            sys.stdout.write('\r')
            time.sleep(0.5)