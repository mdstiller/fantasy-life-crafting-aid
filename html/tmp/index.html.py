# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454778725.952074
_enable_loop = True
_template_filename = u'/home/michael/programming/fantasy-life-crafting-aid/html/index.html'
_template_uri = u'index.html'
_source_encoding = 'ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'theme.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n<div class="content-container">\n\t<div class="content-header">\n\t\tThis website will help you generate ingredient lists for each Life of Fantasy Life!\n\t</div>\n\t<div class="content">\n\t<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum varius maximus metus, in cursus dui ullamcorper sit amet. Morbi faucibus bibendum vehicula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent hendrerit, mi at ultrices congue, sapien ligula interdum diam, non egestas est libero porta tellus. Duis maximus ut risus eu rhoncus. Ut at arcu sed nunc aliquam malesuada. Fusce eget mattis lectus, in aliquam urna. Nullam non finibus orci. Proin rutrum vitae augue nec dictum. Morbi pulvinar nulla a tellus scelerisque pulvinar. Fusce auctor, odio eu pharetra ornare, lorem urna eleifend justo, tincidunt dapibus leo velit non lectus. Donec condimentum eu risus quis tristique. Nullam egestas euismod massa vel ultricies.\n\t</p>\n\t<p>\n\tAliquam euismod ac tortor ac dictum. Sed at tristique orci. Proin bibendum nulla vitae odio dapibus, et accumsan risus vestibulum. Nunc blandit sodales augue ut gravida. Proin a pharetra quam. Nam dapibus et erat vitae sagittis. Maecenas dignissim, enim et feugiat luctus, ipsum lectus rhoncus sapien, id rutrum ex turpis quis dui. Pellentesque ultrices maximus condimentum. Praesent vestibulum consequat neque, ac dapibus quam ornare et. Vivamus nec nisi id dui lacinia egestas placerat sed quam. Duis diam leo, commodo sit amet risus ac, scelerisque lobortis augue. Aenean eu tristique lacus, nec posuere ex. Pellentesque imperdiet, erat porta lobortis ullamcorper, ipsum leo venenatis arcu, at luctus mauris velit a est. Sed dapibus mollis enim, id laoreet erat vulputate et.\n\t<p>\n\t</div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 1, "27": 0, "38": 32}, "uri": "index.html", "filename": "/home/michael/programming/fantasy-life-crafting-aid/html/index.html"}
__M_END_METADATA
"""
