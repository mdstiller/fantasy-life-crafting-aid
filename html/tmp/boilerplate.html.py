# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454778725.963286
_enable_loop = True
_template_filename = u'/home/michael/programming/fantasy-life-crafting-aid/html/boilerplate.html'
_template_uri = u'boilerplate.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->\n<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->\n<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->\n<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->\n    <head>\n        <meta charset="utf-8">\n        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n        <title>Fantasy Life Crafting Aid</title>\n        <meta name="description" content="">\n        <meta name="viewport" content="width=device-width">\n        \n        <script type="text/javascript" src="/static/js/jquery-1.11.3.min.js"></script>\n        <script src="/static/js/bootstrap.min.js"></script>\n\n        <link rel="stylesheet" href="/static/css/normalize.css">\n        <link rel="stylesheet" href="/static/css/bootstrap.css">\n        <link rel="stylesheet" href="/static/css/theme.css">\n    </head>\n    <body>\n        <!--[if lt IE 7]>\n           <p class="chromeframe">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">activate Google Chrome Frame</a> to improve your experience.</p>\n       <![endif]-->\n    ')
        __M_writer(unicode(next.body()))
        __M_writer(u'\n    </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "24": 24, "30": 24, "22": 1, "23": 24}, "uri": "boilerplate.html", "filename": "/home/michael/programming/fantasy-life-crafting-aid/html/boilerplate.html"}
__M_END_METADATA
"""
