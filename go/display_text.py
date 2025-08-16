import pyxel

class DisplayText:
    def __init__(self, position: list, line_gap: int = 2):
        self.position = position.copy()
        self.lines = []
        self.line_gap = line_gap  # extra pixels between lines

    def newLine(self, text: str, color: int = 7):
        self.lines.append({
            "text": text.upper(),
            "color": color
        })
        return self
    
    def update(self):
        pass

    def draw(self):
        if not self.lines:
            return

        # Get longest line width in pixels
        max_width = max(len(line["text"]) for line in self.lines) * pyxel.FONT_WIDTH
        line_height = pyxel.FONT_HEIGHT + self.line_gap
        total_height = len(self.lines) * line_height - self.line_gap  # don't add gap after last line
        
        x = self.position[0] - max_width / 2
        y = self.position[1] - total_height / 2

        # Draw background (with small padding)
        padding = 2
        pyxel.rect(
            int(x - padding),
            int(y - padding),
            int(max_width + padding * 2),
            int(total_height + padding * 2),
            0  # black background
        )

        # Draw text lines with colors
        for i, line in enumerate(self.lines):
            pyxel.text(
                int(x),
                int(y + i * line_height),
                line["text"],
                line["color"]
            )
