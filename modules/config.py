import os

code_root = os.path.abspath(os.path.dirname(__file__)).replace("/modules", "")

tornado_settings = dict(
    static_path = code_root + "/static",
    debug=True,
)
mako_path = code_root + '/html'