$(document).ready(function() {

    // JQuery code

	// First scroll bar
	$( function() {
	  var text_handle = $( "#param1_slider_text" );
	  $( "#param1_slider_obj" ).slider({
	    create: function() {
		  text_handle.text( $( this ).slider( "value" ) );
	    },
	    min: 0,
	    max: 10,
	    value: 5,
	    step: 1,
	    animate: false, //true, false, "fast", "slow" - how long it takes to move if you click away from the box

	    slide: function( event, ui ) {
		  text_handle.text( ui.value );
		  $("#param1_value").val( ui.value );
	    }
	  });
	});


	// Second scroll bar
	$( function() {
	  var text_handle = $( "#param2_slider_text" );
	  $( "#param2_slider_obj" ).slider({
		create: function() { //pre-populate slider with initial value below
		  text_handle.text( $( this ).slider( "value" ) );
	    },
		//set initial parameters
	    min: 0,
	    max: 10,
	    value: 5,
	    step: 1,
	    animate: false,

	    slide: function( event, ui ) {
		  text_handle.text( ui.value );
		  $("#param2_value").val( ui.value );
	    }
	  });	
	});
});