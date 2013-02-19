#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
"""
Custome template tag to capture template tags as variables
"""

# python/django imports
from django import template
from django.utils.safestring import mark_safe

# project import


register = template.Library()


@register.tag(name='captureas')
def do_captureas(parser, token):
    try:
        tag_name, args = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("'captureas' node requires a variable name.")
    nodelist = parser.parse(('endcaptureas',))
    parser.delete_first_token()
    return CaptureasNode(nodelist, args)


class CaptureasNode(template.Node):
    def __init__(self, nodelist, varname):
        self.nodelist = nodelist
        self.varname = varname

    def render(self, context):
        # replace space and new line char with None
        output = self.nodelist.render(context).replace(' ', '').replace('\n', '')

        # tmp fix to check if the string is empty after stripping white spaces
        # and new line char
        if len(output) > 0:
            output = self.nodelist.render(context)

        context[self.varname] = mark_safe(output)
        return ''
