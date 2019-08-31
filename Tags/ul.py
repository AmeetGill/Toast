from tag import tag
from li import li
class ul(tag):
	def __init__(self ,tagId = "",className = "",style = {},childrens = [],inlineStyle={}):
		super().__init__(tagId = tagId, className = className, style = style, childrens = childrens, tagType = "ul", inlineStyle = inlineStyle)
	
	def create_list_from_list(self,data = [], listStyle = {}):
		index = 1
		for elem in data:
			self.childrens.push(li(className = str(index),inlineStyle = listStyle))

	def create_list_from_json(self,jsonObj = {}):
		''' to do '''


