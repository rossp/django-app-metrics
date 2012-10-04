from django import template
from sparkblocks import spark

register = template.Library()

def do_sparkblock(parser, token):
    parts = token.split_contents()
    if len(parts) <= 3:
        raise template.TemplateSyntaxError("%s requires at least two arguments" % parts[0])
    return SparkBlockNode(parts[1:])

class SparkBlockNode(template.Node):
    def __init__(self, parts):
        try:
            self.parts = map(int, parts)
        except:
            self.parts = [0]
    
    def render(self, context):
        return spark(self.parts)

register.tag('sparkblock', do_sparkblock)
