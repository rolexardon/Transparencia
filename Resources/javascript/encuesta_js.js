		$(document).ready(function() {
			var selectedTabIndex = null;
			var validated = false;
			var valorE1 = 0 ;
			var dep=0;
			var fecha = document.getElementById('hidden_date').value;
			$( "#tabs" ).tabs({
			    select: function(event, ui) {
					selectedTabIndex = ui.index;
					var form_2_val = "null";
					if (selectedTabIndex == 0 ) form_2_val = "pg2";
					if (selectedTabIndex == 1 ) form_2_val = "pg1";
					
					switch(form_2_val){
						case "pg1" :
									validate_style(form_2_val,"temporal")
									break
						case "pg2" :
									validate_style(form_2_val,"temporal")
									break
					}
					f = "#" + form_2_val;
					validated = $(f).valid();
					return validated;
    			}
			});
			function validate_style(form,type){
				try{
					switch(form){
						case "pg1":
									if(type=="temporal"){
										$("#hidden_tiposave").val("temporal");
										$("#pg1").validate({
											rules: {

											},
											messages :{	}
										});
										$.validator.addMethod("Numeric_tbxs", $.validator.methods.number, "Ingrese elementos numéricos");
										$.validator.addClassRules("number_inputs", { Numeric_tbxs: true});										
									}
									else {
											$("#hidden_tiposave").val("final");
											$("#pg1").validate({
												onsubmit: false,
												rules: {
													tbx_fecha : "required",
													cbx_centros : "required",
													
												},
												messages :{	}
											});							
									}
									break
						case "pg2":
									if(type=="temporal"){
									    $("#hidden_tiposave2").val("temporal");
										$("#pg2").validate({
											onsubmit: false,
											rules: {
												tbxE_1 : {
															max: $("#D_2").val()
														},
												tbxE_5 : {
															max: $("#D_2").val()
														},
												tbxE_6 : {
															max: $("#D_3").val()
														},
												tbxE_7 : {
															max: Math.max($("#D_2").val(),$("#D_3").val())
														}
											},
											messages :{	
												tbxE_1 : {
															max:"Asegúrese que el valor sea igual o menor que D2._"
														 },
												tbxE_5 : {
															max:"Asegúrese que el valor sea igual o menor que D2._"
														 },	
												tbxE_6 : {
															max:"Asegúrese que el valor sea igual o menor que D3._"
														 },			
												tbxE_7 : {
															max:"Asegúrese que el valor sea igual o menor que el mayor entre D2._ y D3._"
														 }											 
											}				
										});
										$.validator.addMethod("Numeric_tbxs2", $.validator.methods.number, "Ingrese elementos numéricos");
										$.validator.addClassRules("inputs_parteE", { Numeric_tbxs2: true});
									}
									else {
										$("#hidden_tiposave2").val("final");
									
									}
									break								
					}
				}
				catch(err){
					alert(err.description);
				}
			};
			$( "#datepicker" ).datepicker({ 
					dateFormat: 'yy-mm-dd'
					});
			$("#datepicker").datepicker('setDate', fecha); 
			$("#id_centros").change(function(){
				$("#id_codigocentro").empty();
				$("#id_tipocentro").empty();
				$.ajax({
							type:"GET",
							data:
								{
									data : "infodecentro",
									idcentro:$(this).val()
								},
							url: "{% url url_bringcentroinfo %}",
							success: function(lista){
								
									$("#id_codigocentro").val(lista[0]);
									$("#id_tipocentro").val(lista[1]);
							}
				});
			});
			$("#btnSave").click(function(){
				try{
					var selectedTabIndex = $("#tabs").tabs("option", "selected");
					if(selectedTabIndex == 0 ){
						validate_style("pg1","temporal");
						if($("#pg1").valid()) {
							validate_style("pg2","temporal");
							if($("#pg2").valid()) {
								$("#pg1,#pg2").submit();
							}
						}
					}
					else {
						validate_style("pg2","temporal");
						if($("#pg2").valid()) {
							validate_style("pg1","temporal");
							if($("#pg1").valid()) {
								$("#pg2,#pg1").submit();
							}
						}
					}
				}
				catch(err){
					alert(err);
				}				
			});
			$("#btn_Publish").click(function(){
				if(confirm("¿Está seguro que desea publicar la encuesta y guardar los datos permanentemente?")){
				try{
					var selectedTabIndex = $("#tabs").tabs("option", "selected");
					if(selectedTabIndex == 0 ){
						validate_style("pg1","final");
						if($("#pg1").valid()) {
							validate_style("pg2","final");
							if($("#pg2").valid()) {
								$("#pg1,#pg2").submit();
							}
						}
					}
					else {
						validate_style("pg2","final");
						if($("#pg2").valid()) {
							validate_style("pg1","final");
							if($("#pg1").valid()) {
								$("#pg2,#pg1").submit();
							}
						}
					}
				}
				catch(err){
					alert(err);
				}
				}
			});
			$("#cbxF_3").click(function(){
				document.getElementById("cbxF_4").checked = false;
			});
			$("#cbxF_4").click(function(){
				document.getElementById("cbxF_3").checked = false;
			});
			$("#cbxF_5").click(function(){
				if(document.getElementById("cbxF_2").checked == true || document.getElementById("cbxF_4").checked == true){
					document.getElementById("cbxF_5").checked = false;
					}
			});
		});