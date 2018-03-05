//Interface with Python file
var form = document.getElementById('form');



form.addEventListener("submit",function(e) {

	var q = form.elements.question.value;


	console.log("parsing starts...pour"+q);

	
	$.getJSON('/_parse', {q}, function(data) {
										//Display grandpybot's answer
										$("#answer").text(data.result);
										
										console.log(data.result);
										
										//Displays Google Maps iframe
										console.log(data.lnk);
										$('#gmaps').attr("src",data.lnk);
										$('#gmaps').show();
										
									 }
	)
	
	
	//$("#answer").text(question);
	console.log("...parsing done.");
	e.preventDefault();
	
}
)