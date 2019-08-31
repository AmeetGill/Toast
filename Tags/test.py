from html import html
from head import head
from body import body
from h1 import h1
from ul import ul

head = head(title="test page")
h1 = h1(text = "hello")
ul = ul();
ul.create_list_from_list(["he","ha","hy"],{})
childs = [h1,ul]
body = body(childrens = childs)
page = html(head_tag = head,body_tag = body)
page.generate_html()

