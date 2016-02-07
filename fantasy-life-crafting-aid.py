import bcrypt
import concurrent.futures
import MySQLdb
import markdown
import os.path
import re
import subprocess
import torndb
import tornado.escape
from tornado import gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload
import unicodedata

from modules import config, handlers

from tornado.options import define, options
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="database host")
define("mysql_database", default="fantasy_life_crafting_aid", help="database name")
define("mysql_user", default="fl_db_admin", help="database user")
define("mysql_password", default="fl_db_admin", help="database password") 

#define handlers and settings outside of main loop

class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(handlers.tornado_handlers, **config.tornado_settings)
        # Have one global connection to the blog DB across all handlers
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)

    tornado.autoreload.start()

    for filename in os.listdir(config.tornado_settings["template_path"]):
        tornado.autoreload.watch(os.path.abspath(os.path.join(config.tornado_settings["template_path"], filename)))
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()