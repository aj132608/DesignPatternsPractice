class Journal:
    """
    Good Examples of functions
    """

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    """
    Bad Examples of functions
    """
    # def save(self, filename):
    #     pass
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass

