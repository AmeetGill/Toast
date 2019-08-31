class title:
	def __init__(self,title = ""):
		assert(title is not None), "titile must be defined"
		self.tag_string = '<title>{0}</title>'.format(title)


