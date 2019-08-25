class Tag:
	def __init__(self,tagId = "",className = "",style = {},childrens = [],tagType="div",inlineStyle={}):
		assert(tagId is "") , "in {} id must be a string".format(tagType)
		assert(tagType is "") , "in {} tagType must be a string".format(tagType)
		assert(className is ""), "in {} className must be a string".format(tagType)
		assert(style is {}) , "in {} style must be an object".format(tagType)
		assert(inlineStyle is {}) , "in {} inlineStyle must be an object".format(tagType)

		self.tag_string = '<{0} class = "{1}" id = "{2}" style = "{3}">{4}</{0}>'
		self.childrens = childrens
		self.style = style
		self.tagId = tagId
		self.className = className
		self.tagType = tagType
		self.inlineStyle= inlineStyle
	
	def generate(self,childrens,jsonStyleObj):
		tags_string = ""
		for child in childrens:
			tags_string += child.generate_child_tags(jsonStyleObj)
		return tags_string

	def generate_child_tags(self,jsonStyleObj):
		self.checkStylesAreValid(jsonStyleObj)
		child_tag_string =  "" if self.childrens is None else self.generate(self.childrens,jsonStyleObj)
		inline_style_string = "" if self.inlineStyle is None else self.generate_style_obj_string(jsonStyleObj)
		self.tag_string.format(self.tagType,self.className,self.tagId,inline_style_string,child_tag_string)


	def checkStylesAreValid(self,jsonStyleObj):
		for key,  in self.style.__dict__.items():
			if(key not in jsonStyleObj):
				raise Exception("in {} '{}' is not a valid style attribute".format(self.tagType,key))
		for key,  in self.inlineStyle.__dict__.items():
			if(key not in jsonStyleObj):
				raise Exception("in {} '{}' is not a valid style attribute".format(self.tagType,key))

	def generate_style_obj_string(self,jsonStyleObj):
		str = ""
		for key,  in self.inlineStyle.__dict__.items():
			str += jsonStyleObj[key]+ "=" + self.inlineStyle[key] + ";"  
		return str