from enum import IntEnum

from colorama import Fore, Style

class StyleOrder(IntEnum):
    # styles are defined
    # in the same order as the notebook
    TL = 0 # top-left
    H = 1,  # horiz
    TR = 2
    V = 3
    BL = 4
    BR = 5

STYLES = {
    'thin': ("\u250c\u2500\u2510" "\u2502" "\u2514\u2518"),
    'regular': ("\u250f\u2501\u2513" "\u2503" "\u2517\u251b"),
}

class Box1:

    def __init__(self, w, h, *, style='regular', color=None):
        """
        use e.g. color = Fore.RED if not plain black
        """
        self.w = w
        self.h = h
        self.color = color
        try:
            self.style = STYLES[style]
        except KeyError:
            raise ValueError(f"unknown style {style}")
        if w < 2 or h < 2:
            raise ValueError(f"box dimension must be >= 2")


    def raw_box(self):
        result = ""
        # for shorter fomulas
        s = self.style
        O = StyleOrder
        # first line
        result += s[O.TL] + (self.w-2)*s[O.H] + s[O.TR] + "\n"
        # middle lines
        for _ in range(self.h-2):
            result += s[O.V] + (self.w-2)*' ' + s[O.V] + "\n"
        # last line
        result += s[O.BL] + (self.w-2)*s[O.H] + s[O.BR]
        return result

    def colored(self, text):
        return text if not self.color else f"{self.color}{text}{Style.RESET_ALL}"

    def box(self):
        return self.colored(self.raw_box())


class Box2(Box1):
    def __str__(self):
        return self.box()
