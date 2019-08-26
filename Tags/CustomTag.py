from Tag import Tag
class CustomTag(Tag):
    def __init__(self,customGenerator,*args):
        self.custom_generator_func = customGenerator
        self.custom_generator_args = args

    def custom_generator(self,*args):
        tag_str_output = self.custom_generator_func(args)
        assert(tag_str_output is ""), "output of your {} custom generator should be a string".format("curtom Tag")
        return tag_str_output

    def generator(self):
        if(self.custom_generator):
            return self.custom_generator(self.args)