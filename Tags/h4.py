from tag import tag


class h4(tag):
    def __init__(self, tagId="", className="", style=None, children=None, inlineStyle=None, text=""):
        super().__init__(tagId=tagId, className=className, style=style, children=children, tagType="h4",
                         inlineStyle=inlineStyle, text=text)
