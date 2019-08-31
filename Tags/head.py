class head:
	def __init__(self,title = ""):
		self.tag_string = '<title>{0}</title>'.format(title)

    def generate(self,childrens,jsonStyleObj):
		tags_string = ""
		for child in childrens:
			tags_string += child.generate_child_tags(jsonStyleObj)
		return tags_string

