import json
class Html:
	def __init__(self):
		self.tag_string = "<html>{}</html>"
		self.children_tag = None
	
	def generate_html(self):
		jsonStyleObj = {}
		with open('../style/parsed_style.json') as f:
			jsonStyleObj = json.load(f)
		print(self.tag_string.format(self.children_tag.generate(jsonStyleObj)))