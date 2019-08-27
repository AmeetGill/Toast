from tag import tag
class li(tag):
	def __init__(self ,tagId = "",className = "",style = {},childrens = [],inlineStyle={}):
		super().__init__(tagId = tagId, className = className, style = style, childrens = childrens, tagType = "li", inlineStyle = inlineStyle)