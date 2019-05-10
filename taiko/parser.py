class Parser:

    def __init__(self, file):
        self.file = file

        self.name = ""
        self.author = ""
        self.bpm = 0

    def parse(self):
        with open(self.file, "rb") as f:
            file = f.read()
