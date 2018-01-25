$( document ).ready(function() {
    $(".sky").click(function(){
        $(this).hide();
    });
    $("#reset").click(function(){
        $("img").show();
    });
})