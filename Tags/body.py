from tag import tag;
class body(tag):
    def __init__(self,style = {},childrens = [],inlineStyle={}):
        super.__init__(style = style, childrens = childrens,tagType = "body",inlineStyle=inlineStyle)