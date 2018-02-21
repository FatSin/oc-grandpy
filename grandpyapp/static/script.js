//alert('Hello!');

var form = document.getElementById('form');
//var question = document.getElementById('question').textContent;
var question = form.elements.question.value;

form.addEventListener("submit",function(e) {
	alert(question);
	console.log(question);
	})