class Tag:
	def __init__(self,tagId = "",className = "",style = {},childrens = [],tagType="div",inlineStyle={}):
		assert(tagId is "") , "id must be a string"
		assert(tagType is "") , "tagType must be a string"
		assert(className is ""), "className must be a string"
		assert(style is {}) , "style must be an object"
		assert(inlineStyle is {}) , "inlineStyle must be an object"

		self.tag_string = '<{0} class = "{1}" id = "{2}" style = "{3}">{4}</{0}>'
		self.childrens = childens
		self.style = style
		self.tagId = tagId
		self.className = className
		self.tagType = tagType
		self.inlineStyle= inlineStyle

	def generate(self,jsonStyleObj):
		self.checkStylesAreValid(jsonStyleObj)
		child_tag_string =  "" if childrens is None else self.generate(self.childrens,jsonStyleObj)
		inline_style_string = "" if self.inlineStyle is None else self.generate_style_obj_string(jsonStyleObj)
		tags_string.format(self.tagType,self.className,self.tagId,child_tag_string)

	def generate(self,childens,jsonStyleObj):
		tags_string = ""
		for child in childrens:
			tags_string += child.generate(jsonStyleObj)
		return tags_string 

	def checkStylesAreValid(self,jsonStyleObj):
		for key, value in self.style.__dict__.items():
			if(key not in jsonStyleObj):
				raise Exception("'"+key+"' is not a valid style attribute")
		for key, value in self.inlineStyle.__dict__.items():
			if(key not in jsonStyleObj):
				raise Exception("'"+key+"' is not a valid style attribute")

	def generate_style_obj_string(self,jsonStyleObj):
		str = ""
		for key, value in self.inlineStyle.__dict__.items():
			str += jsonStyleObj[key]+ "=" + self.inlineStyle[key] + ";"  
		return str;