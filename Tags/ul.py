from tag import tag
from li import li


class ul(tag):
    def __init__(self, tagId="", className="", style={}, children=[], inlineStyle={}):
        super().__init__(tagId=tagId, className=className, style=style, children=children, tagType="ul",
                         inlineStyle=inlineStyle, text="")

    def create_list_from_list(self, data=None, listStyle=None):
        if listStyle is None:
            listStyle = {}
        if data is None:
            data = []
        index = 1
        for elem in data:
            self.children.append(li(className=str(index), text=elem, inlineStyle=listStyle))

    def create_list_from_json(self, jsonObj=None):
        ''' to do '''
        if jsonObj is None:
            jsonObj = {}
