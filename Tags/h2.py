from tag import tag
class h2(tag):
	def __init__(self ,tagId = "",className = "",style = {},childrens = [],tagType="div",inlineStyle={},text = ""):
		super().__init__(tagId = tagId, className = className, style = style, childrens = childrens, tagType = "h2", inlineStyle = inlineStyle,text=text)
		

