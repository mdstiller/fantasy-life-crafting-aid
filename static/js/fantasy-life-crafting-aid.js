jQuery(function($){
	$("#ingredient-1").qtip({
        style: { classes: 'qtip-wiki' },
        content: {
            text: function(event, api) {
                api.elements.content.html('Loading...');
                return $.ajax({
                    url: '/page/life-ingredient-tooltip?tooltip-ingredients-id=1'
                    })
                    	.then(function(content) {
                        	api.elements.content.html(content);
                        	}, function(xhr, status, error) {
                        	api.set('content.text', status + ':  ' + error);
                        	});
                        },
                    title: {text: 'Ingredient Information'}
        }
	});
});