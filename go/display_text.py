import pyxel

class DisplayText:
    def __init__(self, position: list):
        self.position = position.copy()
        self.lines = []

    def newLine(self, text: str):
        self.lines.append(text)
        return self

    def draw(self):
        if not self.lines:
            return

        # Get longest line width in pixels
        max_width = max(len(line) for line in self.lines) * pyxel.FONT_WIDTH
        line_height = pyxel.FONT_HEIGHT
        total_height = len(self.lines) * line_height
        
        x = self.position[0] - max_width / 2
        y = self.position[1] - total_height / 2

        # Draw background (with small padding)
        padding = 2
        pyxel.rect(
            x - padding,
            y - padding,
            max_width + padding * 2,
            total_height + padding * 2,
            0  # black background
        )

        # Draw text lines
        for i, line in enumerate(self.lines):
            pyxel.text(x, y + i * line_height, line, 7)  # white text
