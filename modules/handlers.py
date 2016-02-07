import tornado.web

from mako.lookup import TemplateLookup

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
    
    def __init__(self, application, request, transforms=None):
        mako_root = "/home/michael/programming/fantasy-life-crafting-aid/html"
        mako_tmp_root = mako_root + "/tmp/"
 
        tornado.web.RequestHandler.__init__(self, application, request)
        self.lookup = TemplateLookup(
            directories=[mako_root],
            module_directory=mako_tmp_root,
            output_encoding='utf-8', encoding_errors='replace')

    def render_template(self, template_name, **kwargs):
        new_template = self.lookup.get_template(template_name)
        
        #test
        print(template_name)

        #def f1(p1):
        #    print p1
        #f1(kwargs)
        #test

        contents = new_template.render(**kwargs)
        #contents = new_template.render(lives="A test life", lives_again="More lives!")

        if contents:
            self.write(contents)
        else:
            return False

class PageHandler(BaseHandler):
    def get(self, page=None):
        self.render_template(page + ".html")

class MainHandler(BaseHandler):
    def get(self):
        self.render_template("index.html")

class LifeOverviewHandler(BaseHandler):
    def get(self):
        handler_lives = "Sample Life Code"
        #lives = self.db.query("SELECT * FROM lives ORDER BY lives_name")  
        self.render_template("life-overview.html", dict(lives="A test life", lives_again="More lives!"))      

tornado_handlers = [
    (r"/", MainHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "/home/michael/programming/fantasy-life-crafting-aid/static"}),
    (r"/page/([a-zA-Z_.-]+)", PageHandler),
    (r"/page/life-overview", LifeOverviewHandler)
]