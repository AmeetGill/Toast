from Tag import Tag
class CustomTag(Tag):
    def __init__(self,customGenerator,*args):
        self.custom_generator = customGenerator

    def custom_generator(self,*args):
        tag_str_output = self.custom_generator(args)
        assert(tag_str_output is ""), "output of your {} custom generator should be a string".format("curtom Tag")




