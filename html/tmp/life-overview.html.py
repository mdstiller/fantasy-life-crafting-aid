# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454778784.500495
_enable_loop = True
_template_filename = u'/home/michael/programming/fantasy-life-crafting-aid/html/life-overview.html'
_template_uri = u'life-overview.html'
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
        lives = context.get('lives', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div class="content-container">\n\t<div class="content-header">\n\t\tTODO: Generate list of all Lives that allow for crafting.\n\t</div>\n\t<div class="content">\n\t\t')
        __M_writer(unicode(lives))
        __M_writer(u'\n\t</div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"33": 1, "34": 7, "27": 0, "35": 7, "41": 35}, "uri": "life-overview.html", "filename": "/home/michael/programming/fantasy-life-crafting-aid/html/life-overview.html"}
__M_END_METADATA
"""
