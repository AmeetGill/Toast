class tag:
	def __init__(self,tagId:str = "",className:str = "",style = {},childrens = [],tagType:str ="div",inlineStyle={},text:str=""):
		self.tag_string = '<{tagType} class = "{className}" id = "{tagId}" style = "{inline_style_string}">{child_tag_string}</{tagType}>'
		self.childrens = childrens
		self.style = style
		self.tagId = tagId
		self.className = className
		self.tagType = tagType
		self.inlineStyle= inlineStyle
		self.text = text
	
	def generate_child_tags(self,childrens,jsonStyleObj):
		tags_string = ""
		print(self.tagType + str(childrens))
		for child in childrens:
			tags_string += child.generate(jsonStyleObj)
		return tags_string

	def generate(self,jsonStyleObj):
		#self.checkStylesAreValid(jsonStyleObj)
		child_tag_string =  "" if self.childrens is None else self.generate_child_tags(self.childrens,jsonStyleObj)
		#inline_style_string = "" if self.inlineStyle is None else self.generate_style_obj_string(jsonStyleObj)
		inline_style_string = ""
		generated = self.tag_string.format(tagType = self.tagType,className = self.className,tagId = self.tagId,inline_style_string = inline_style_string,child_tag_string = child_tag_string+self.text)
		return generated

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