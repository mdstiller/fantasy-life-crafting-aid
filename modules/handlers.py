import tornado.web
import config

from mako.lookup import TemplateLookup

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
    
    def __init__(self, application, request, transforms=None):
        tornado.web.RequestHandler.__init__(self, application, request)
        self.lookup = TemplateLookup(
            directories=[config.mako_path],
            module_directory=config.mako_path + "/tmp/",
            output_encoding='utf-8', encoding_errors='replace')

    def render_template(self, template_name, **kwargs):
        try:
            new_template = self.lookup.get_template(template_name)
            
            print(template_name)
            contents = new_template.render(**kwargs)

            if contents:
                self.write(contents)
            else:
                return False
        except:
            print "template error"

class PageHandler(BaseHandler):
    def get(self, page=None):
        self.render_template(page + ".html")

class MainHandler(BaseHandler):
    def get(self):
        self.render_template("index.html")

class LifeOverviewHandler(BaseHandler):
    def get(self):
        #lives = self.db.query("SELECT * FROM lives ORDER BY lives_name")  

        test_data = {
            "lives":"A test life",
            "lives_again":"More lives!"
        }
        self.render_template("life-overview.html", data=test_data)      

tornado_handlers = [
    (r"/", MainHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "/home/michael/programming/fantasy-life-crafting-aid/static"}),
    (r"/page/life-overview", LifeOverviewHandler),
    (r"/page/([a-zA-Z_.-]+)", PageHandler),
]