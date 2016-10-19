var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;


class SubmitEmpleado extends Backbone.View
{

	initialize()
	{
		this.empleado = {};
		this.template = _.template($("#").html());
		this.render();
	}

	events()
	{
		return { 
				"submit #form" : "verificar",
			   };
	}
	verificar(e)
	{
		this.empleado = 
		{
			"apellido_paterno"				  : $("#id_model_form_empleado-apellido_paterno").val(),
			"apellido_materno" 				  : $("#id_model_form_empleado-apellido_materno").val(),
			"nombre" 		  				  : $("#id_model_form_empleado-nombre").val(),
			"numero_documento_identificacion" : $("#id_model_form_empleado-numero_documento_identificacion").val(),
		}
	}
	text_box_null(textbox)
	{
		if(textbox.val() == "" textbox.val().lenght() == )
	}
    render() 
	{
     	this.$el.html(this.template());
		return this;
    }

}

module.exports = SubmitEmpleado;
