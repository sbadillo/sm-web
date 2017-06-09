$(document).ready(function(){

	// Script that adds slideout property to whole content section
	
	$('#activate-slideout').click(function() {
		console.log($(this).attr("class")); 		// reads classes of clicked element
	    $('.content').toggleClass('slideout');			// slidesout content element

        $('#project-details').toggleClass('expanded');

	});

	// Need to do this for each element: 
	// 1. get name/slug of project on click, maybe the slug is included as the class 
	// 2. pull project description from md file <-- jinja?
	// 3. populates a div with that description.
	// 4. 


})



