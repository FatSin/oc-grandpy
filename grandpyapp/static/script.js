var form = document.getElementById('form');

var mq = window.matchMedia("(min-width: 500px)")

if(!mq.matches){
	$('#bubble_img').attr("src",'/static/images/bubble_down.png');
	$('#gmaps').attr("width",'300');
	$('#gmaps').attr("height",'180');
}


form.addEventListener("submit",function(e) {

	var q = form.elements.question.value;

	console.log("parsing starts...pour"+q);
	
	$('#grandpy').addClass('gprotate');
	var knownLocation = 0;
	
	//Interface with Python
	$.getJSON('/_callPython', {q}, function(data) {
										
										//$('#grandpy').addClass('gprotate');
										//Display grandpybot's answer
										
										if(mq.matches){
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
										
											$('#link_wiki').css("margin-top","-30px");
											$('#link_wiki').css("margin-left","-70px");
										}
										
										else{
											if (data.result.length >= 320){
												$("#answer").css("font-size","11px"); 
											 }
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
										
									 }
									 
									 
									 
	)

retry.addEventListener("click",function(e) {

			$('#grandpy').attr("src",'/static/images/gp_normal.png');
			$('#question').val('');
			$('#answer').text('Dis-moi où tu veux aller.');		
			$('#retry').addClass('invisible');
			$('#question').removeClass('invisible');
			$('#send').removeClass('invisible');
			$('#link_wiki').hide();
			$('#gmaps').addClass('invisible');
			e.preventDefault();
			
			if(mq.matches){
				$("#answer").css("margin-top","-120px");
				$("#answer").css("padding-left","120px");
				$("#bubble_img").css("height","100%");
			}
});
	
	console.log("...parsing done.");
	e.preventDefault();
	
	
}
)