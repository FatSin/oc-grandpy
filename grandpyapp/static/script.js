//Interface with Python file
var form = document.getElementById('form');



form.addEventListener("submit",function(e) {

	var q = form.elements.question.value;


	console.log("parsing starts...pour"+q);
	
	//Display Grandpy's "thinking faces" with timers
	$('#grandpy').attr("src",'/static/images/gp_left.png');

	
	$.getJSON('/_parse', {q}, function(data) {
										//Display grandpybot's answer
										$("#answer").text(data.result);
										//$('#bubble').show();
										$('#bubble').css('visibility', 'visible');
										console.log(data.result);
										
										//Displays Google Maps iframe
										console.log(data.lnk);
										$('#gmaps').attr("src",data.lnk);
										//$('#gmaps').show();
										('#gmaps').css('visibility', 'visible');
										$('#link_wiki').attr("href",data.wiki);
										$('#link_wiki').show();
										console.log("lien wiki"+data.wiki);
										
										//Display Grandpy's "normal face"
										$('#grandpy').attr("src",'/static/images/gp_answers.png');
									 }
	)
	
	
	//$("#answer").text(question);
	console.log("...parsing done.");
	e.preventDefault();
	
}
)