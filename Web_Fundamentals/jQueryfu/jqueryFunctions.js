$( document ).ready(function() {
  $( "#clickme" ).click(function() {
    $( "#jungle" ).slideToggle( "slow");
    });

  $( "#fader" ).click(function() {
    $( "#desert" ).fadeIn( "slow")
    });

  $( "#outer").click(function(){
    $( "#tundra").fadeOut( "fast")
    });

  $( "#addClass p:last").addClass("selected");

  $( "#hidefunc").click(function(){
    $("#hider").hide("slow")
    });
  $( "#showfunc").click(function(){
      $("#shower").show("slow")
    });
  $( "#tog").click(function(){
      $(".forest").toggle("slow")
    });
  $( "#sD").click(function(){
      $("#mountains").slideDown("slow")
    });
  $( "#slider").click(function(){
      $("#ocean").slideUp("slow")
    });
  $( "#beforefunc p").before( "<b>Hello</>");
  $( "#afterfunc h2").after( "<b>Hello</>");
  $( "#app h3" ).append( "<f>  Hello</f>" );
  $( "#var button" ).click(function() {
    var text = $( this ).text();
    $( "var_in" ).val( text );
  });





})
