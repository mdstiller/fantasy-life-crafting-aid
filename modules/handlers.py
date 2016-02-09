import tornado.web
import config
import simplejson

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
        #try:
            new_template = self.lookup.get_template(template_name)
            contents = new_template.render(**kwargs)

            if contents:
                self.write(contents)
            else:
                return False
        #except:
        #    print "template error"

class PageHandler(BaseHandler):
    def get(self, page=None):
        self.render_template(page + ".html")

class MainHandler(BaseHandler):
    def get(self):
        self.render_template("index.html")

class DataEntryHandler(BaseHandler):
    def get(self):
        self.render_template("admin-data-entry.html")

class LifeOverviewHandler(BaseHandler):
    def get(self):
        ingredients_recset = self.db.query("SELECT * FROM ingredients ORDER BY ingredients_name")
        print ingredients_recset[0].ingredients_name

        ui_data = []
        for row in ingredients_recset:
            ui_data.append({
                'id': row.ingredients_id,
                'name': row.ingredients_name,
                'found': row.ingredients_found
            })

        ingredient_json = simplejson.dumps(ui_data)

        self.render_template("life-overview.html", ingredients=ingredients_recset, ingredientjson=ingredient_json)      

class LifeIngredientTooltipHandler(BaseHandler):
    def get(self):       
        self_ingredients_id = self.get_argument("tooltip-ingredients-id") 
        print "Ingredients ID: " + self_ingredients_id
        self_query = "SELECT * FROM ingredients WHERE ingredients_id = '" + self_ingredients_id + "'"
        ingredients_recset = self.db.query(self_query)
        
        print str(ingredients_recset[0].ingredients_id) + ":" + ingredients_recset[0].ingredients_name

        self.render_template("life-ingredient-tooltip.html", ingredients=ingredients_recset)


tornado_handlers = [
    (r"/", MainHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "/home/michael/programming/fantasy-life-crafting-aid/static"}),
    (r"/page/life-overview", LifeOverviewHandler),
    (r"/page/life-ingredient-tooltip", LifeIngredientTooltipHandler),
    (r"/page/([a-zA-Z_.-]+)", PageHandler),
]