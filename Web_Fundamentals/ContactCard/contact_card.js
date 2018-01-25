$( document ).ready(function(){
    // alert("hello!")
    $('#submit').click(function(){
        var fn= $('#fn').val();
        var ln= $('#ln').val();
        var desc = $('#text').val();
        $('#right').append("<div id='card'><p>"+ fn + " "+ ln + "</p><p id ='back'>" +desc+ "</p></div>");
        $('#fn').val("");
        $('#ln').val("");
        $('#text').val("");    
        return false;
    })
    $(document).on('click', '#card', function(){
        $(this).children().toggle();
    });
    
})