from tag import tag
class h1(tag):
	def __init__(self ,tagId = "",className = "",style = {},childrens = [],tagType="div",inlineStyle={},text = ""):
		super().__init__(tagId = tagId, className = className, style = style, childrens = childrens, tagType = "h1", inlineStyle = inlineStyle,text=text)
		

