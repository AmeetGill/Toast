from tag import tag
class p(tag):
    def __init__(self, tagId="", className="", style={}, childrens=[], inlineStyle={}, text=""):
        super().__init__(tagId=tagId, className=className, style=style, childrens=childrens, tagType="p",
                         inlineStyle=inlineStyle, text=text)


