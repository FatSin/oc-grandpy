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
										 if (data.result.length >= 320){
											 $('#bubble_img').css("height","210");
											 $("#answer").css("margin-top","-190px"); 
											$("#answer").css("padding-left","20px"); 
											
											console.log('gros texte!');
										 }
										 else{
											//$('#bubble_img').attr("height","100%");
											$("#answer").css("margin-top","-160px");
											$("#answer").css("padding-left","20px");
											console.log('normal texte!');
										 }
										
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
											$('#link_wiki').css("margin-top","-30px");
											$('#link_wiki').css("margin-left","-70px");
											$('#link_wiki').css("display","inline");
											$('#link_wiki').show();
											console.log("lien wiki"+data.wiki);
											knownLocation++;
										}
										
								
										
										$('#grandpy').removeClass('gprotate');	
										$('#question').addClass('invisible');								
										$('#send').addClass('invisible');
										$('#retry').removeClass('invisible');
										
										if (knownLocation >=2){
											$('#grandpy').attr("src",'/static/images/gp_answers.png');
										}
										else{
											$('#grandpy').attr("src",'/static/images/gp_hard.png');
										}
										
										/*var retry = document.getElementById('retry');
										retry.addEventListener("click",function(e) {


														$('#retry').addClass('invisible');
														$('#question').removeClass('invisible');
														$('#send').removeClass('invisible');
										
										
										
										});
										*/
									 }
									 
									 
									 
	)

retry.addEventListener("click",function(e) {

			$('#grandpy').attr("src",'/static/images/gp_normal.png');
			$('#question').val('');
			$('#answer').text('Dis-moi où tu veux aller.');
			$("#answer").css("margin-top","-120px");
			$("#answer").css("padding-left","120px");
			$("#bubble_img").css("height","100%");
			$('#retry').addClass('invisible');
			$('#question').removeClass('invisible');
			$('#send').removeClass('invisible');
			$('#link_wiki').hide();
			$('#gmaps').addClass('invisible');
			e.preventDefault();

});
	
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