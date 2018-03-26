//Interface with Python file
var form = document.getElementById('form');



form.addEventListener("submit",function(e) {

	var q = form.elements.question.value;


	console.log("parsing starts...pour"+q);
	
	//Display Grandpy's "thinking faces" with timers
	//$('#grandpy').attr("src",'/static/images/gp_left.png');
	$('#grandpy').addClass('gprotate');

	var knownLocation = 0;
	
	
	
	$.getJSON('/_callPython', {q}, function(data) {
										//$('#grandpy').addClass('gprotate');
										//Display grandpybot's answer
										$("#answer").text(data.result);
										//$('#bubble').show();
										//$('#bubble').css('visibility', 'visible');
										$('#bubble').removeClass('invisible');
										console.log(data.result);
										
										
										if (typeof data.lnk !== 'undefined') {

											//Displays Google Maps iframe
											console.log(data.lnk);
											$('#gmaps').attr("src",data.lnk);
											//$('#gmaps').show();
											//('#gmaps').css('visibility', 'visible');
											$('#gmaps').removeClass('invisible');
											knownLocation++;
										}
										
										
										if (typeof data.wiki !== 'undefined') {
											$('#link_wiki').attr("href",data.wiki);
											$('#link_wiki').show();
											console.log("lien wiki"+data.wiki);
											knownLocation++;
										}
										
										
										$('#grandpy').removeClass('gprotate');
									 }
									 
									 
									 
	)
	
	//Display Grandpy's "normal face"
	
	
	/*
	if (knownLocation >=1){
		$('#grandpy').attr("src",'/static/images/gp_answers.png');
	}
	else{
		$('#grandpy').attr("src",'/static/images/gp_hard.png');
	}
	*/
	
	//$("#answer").text(question);
	console.log("...parsing done.");
	e.preventDefault();
	
	
}
)