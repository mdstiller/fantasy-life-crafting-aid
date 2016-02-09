jQuery(function($){
	$(".ingredient-tooltip").qtip({
        style: { classes: 'qtip-wiki' },
        content: {
            text: function(event, api) {
                var self = $(this);
                var body = "";
                $.each(ingredientjson, function(k, v){
                    if(v["id"] == self.data('id')){
                        console.log(v)
                        body = "Name: " + v["name"] + "</br>";
                        body += "Found: " + v["found"];

                        api.elements.content.html(body);
                    }
                });
                
                return body;
            },
            title: {text: 'Ingredient Information'}
        }
	});
});