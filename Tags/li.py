from tag import tag


class li(tag):
    def __init__(self, tagId="", className="", style=None, children=None, inlineStyle=None, text=""):
        super().__init__(tagId=tagId, className=className, style=style, children=children, tagType="li",
                         inlineStyle=inlineStyle, text=text)
