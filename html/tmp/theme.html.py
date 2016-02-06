# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454778725.959376
_enable_loop = True
_template_filename = u'/home/michael/programming/fantasy-life-crafting-aid/html/theme.html'
_template_uri = u'theme.html'
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
    return runtime._inherit_from(context, u'boilerplate.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n \n<!---body: _global/theme.html--->\n<header>\n    <nav class="navbar navbar-default navbar-fixed-top">\n      <div class="container-fluid">\n        <!-- Brand and toggle get grouped for better mobile display -->\n        <div class="navbar-header">\n          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n          </button>\n          <a class="navbar-brand" href="/page/index">Fantasy Life Crafting Aid</a>\n        </div>\n\n        <!-- Collect the nav links, forms, and other content for toggling -->\n        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n          <ul class="nav navbar-nav">\n            <li class="dropdown">\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Quick Nav<span class="caret"></span></a>\n              <ul class="dropdown-menu">\n                <li><a href="/page/life-overview">Life Overviews</a></li>\n                <li role="separator" class="divider"></li>\n                <li><a href="/page/life-crafts-list">Blacksmith</a></li>\n              </ul>\n            </li>\n          </ul>\n          <form class="navbar-form navbar-left" role="search">\n            <div class="form-group">\n              <input type="text" class="form-control" placeholder="Search">\n            </div>\n            <button type="submit" class="btn btn-default">Submit</button>\n          </form>\n          <ul class="nav navbar-nav navbar-right">\n            <li><a href="#">About...</a></li>                   \n          </ul>\n        </div><!-- /.navbar-collapse -->\n      </div><!-- /.container-fluid -->\n    </nav>\n</header>          \n<header class="logo">\n    <img src="/static/images/logo.png">\n</header>  \n')
        __M_writer(unicode(self.body()))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"40": 34, "33": 1, "34": 46, "27": 0}, "uri": "theme.html", "filename": "/home/michael/programming/fantasy-life-crafting-aid/html/theme.html"}
__M_END_METADATA
"""
