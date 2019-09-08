import json
class html:
	def __init__(self,head_tag,body_tag):
		self.tag_string = "<html>{}</html>"
		self.head_tag = head_tag
		self.body_tag = body_tag
	
	def generate_html(self):
		with open('../style/parsed_style.json') as f:
			jsonStyleObj = json.load(f)
		print(self.tag_string.format(self.head_tag.generate(jsonStyleObj)+self.body_tag.generate(jsonStyleObj)))