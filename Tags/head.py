class head:
	def __init__(self):
		self.tag_string = "<head style = '{}'>{}</head>"
		self.childrens = []
		self.style = {}

	def generate(self):
		child_tag_string =  "" if childrens is None else self.generate(self.childrens) 
		style_obj_string = generate_style_obj_string(self.style)
		tags_string.formate(style_obj_string,child_tag_string)


	def generate(self,childens):
		tags_string = ""
		for child in childrens:
			tags_string += child.generate()

		return tags_string 

	def generate_style_obj_string(self,style):
		for key, value in style.__dict__.items():
        	