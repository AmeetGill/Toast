class head:
    def __init__(self,title:str ="default title"):
        self.tag_string = "<head><title>{0}</title></head>"
        self.title = title

    def generate(self,jsonObj):
        return self.tag_string.format(self.title)