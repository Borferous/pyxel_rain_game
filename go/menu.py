import pyxel
from typing import Callable

class Menu:
    def __init__(self, position: list = None):
        self.position = position.copy() if position else None
        self.options = []
        self.idx = 0
        self.title = None

    def Title(self, text: str):
        self.title = text.upper()
        return self

    def Option(self, label: str, fn: Callable):
        self.options.append({
            "label": label.upper(),
            "fn": fn
        })
        return self

    def update(self):
        if not self.options:
            return

        # Up
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_W):
            self.idx = (self.idx - 1) % len(self.options)

        # Down
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            self.idx = (self.idx + 1) % len(self.options)

        # Select
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE):
            option = self.options[self.idx]
            if "fn" in option and callable(option["fn"]):
                option["fn"]()

    def draw(self):
        if not self.options:
            return

        line_height = 10
        title_height = line_height if self.title else 0

        # Measure width based on longest text (title included)
        texts = [opt["label"] for opt in self.options]
        if self.title:
            texts.append(self.title)

        width = max(pyxel.FONT_WIDTH * (len(t) + 2) for t in texts) + 8
        height = len(self.options) * line_height + 4 + title_height

        # Position (center if none was given)
        if self.position:
            x, y = self.position[0] - width / 2, self.position[1] - height / 2
        else:
            x = (pyxel.width - width) // 2
            y = (pyxel.height - height) // 2

        # Draw background
        pyxel.rect(x - 2, y - 2, width + 4, height + 4, 0)

        # Draw title
        if self.title:
            tx = x + (width - pyxel.FONT_WIDTH * len(self.title)) // 2
            pyxel.text(tx, y + 2, self.title, 11)  # cyan title
            y += title_height  # shift options down

        # Draw options
        for i, option in enumerate(self.options):
            label = option["label"]
            if i == self.idx:
                text = f"> {label}"
                color = 10  # yellow
            else:
                text = f"  {label}"
                color = 7   # white
            pyxel.text(x + 4, y + i * line_height + 2, text, color)
