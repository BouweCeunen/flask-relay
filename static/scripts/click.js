


$(document).on('click', 'label', function () { 
	click($(this).attr('id'));
	return false;
});

function click(id){
	$("#button" + id).attr("disabled", false);
	if($("#button" + id).is(':checked')){
		$("#button" + id).prop("checked", false);
		execute("/con" + id + "/off")
	} else{
		$("#button" + id).prop("checked", true);
		execute("/con" + id + "/on")
	}
}

function execute(req){
    $.getJSON(req, {}, function(data) {})
}


