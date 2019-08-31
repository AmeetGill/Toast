from tag import tag;
class body(tag):
    def __init__(self ,tagId = "",className = "",style = {},childrens = [],tagType="div",inlineStyle={},text = ""):
        super().__init__(tagId = tagId, className = className, style = style, childrens = childrens, tagType = "body", inlineStyle = inlineStyle,text=text)