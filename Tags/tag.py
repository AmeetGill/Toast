class tag:
    def __init__(self, tagId: str = "", className: str = "", style=None, children=None, tagType: str = "div",
                 inlineStyle=None, text: str = ""):
        if inlineStyle is None:
            inlineStyle = {}
        if children is None:
            children = []
        if style is None:
            style = {}
        self.tag_string = '<{tagType} class = "{className}" id = "{tagId}" style = "{inline_style_string}">{' \
                          'child_tag_string}</{tagType}> '
        self.children = children
        self.style = style
        self.tagId = tagId
        self.className = className
        self.tagType = tagType
        self.inlineStyle = inlineStyle
        self.text = text

    @staticmethod
    def generate_child_tags(children, jsonStyleObj):
        tags_string = ""
        for child in children:
            tags_string += child.generate(jsonStyleObj)
        return tags_string

    def generate(self, jsonStyleObj):
        self.check_styles_are_valid(jsonStyleObj)
        child_tag_string = "" if self.children is None else self.generate_child_tags(self.children, jsonStyleObj)
        inline_style_string = "" if self.inlineStyle is None else self.generate_style_obj_string(jsonStyleObj)
        generated = self.tag_string.format(tagType=self.tagType, className=self.className, tagId=self.tagId,
                                           inline_style_string=inline_style_string,
                                           child_tag_string=child_tag_string + self.text)
        return generated

    def check_styles_are_valid(self, jsonStyleObj):
        for key in self.style:
            if key not in jsonStyleObj:
                raise Exception("in {} '{}' is not a valid style attribute".format(self.tagType, key))
        for key in self.inlineStyle:
            if key not in jsonStyleObj:
                raise Exception("in {} '{}' is not a valid style attribute".format(self.tagType, key))

    def generate_style_obj_string(self, jsonStyleObj):
        cssString = ""
        for key in self.inlineStyle:
            cssString += jsonStyleObj[key] + "=" + self.inlineStyle[key] + ";"
        return cssString

    def generate_css_file(self, jsonStyleObj):
        cssString = ""
        for key in self.inlineStyle:
            cssString += jsonStyleObj[key] + "=" + self.inlineStyle[key] + ";"
        return cssString
