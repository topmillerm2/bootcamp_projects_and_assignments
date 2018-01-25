$(document).ready(function(){

    //name, img, types, height, weight
    for(var i = 1; i<=151; i++){
        var pokeImg = "<img src= 'http://pokeapi.co/media/img/" + i + ".png' data-pokenum='"+i+"'>";
        $('#container').append(pokeImg)
    }

    $('img').click(function(){
    var pokeNum = $(this).data("pokenum");

    var url ="https://pokeapi.co/api/v1/pokemon/"+pokeNum+"/";
    $.get(url, function(response){
       htmlBuilder(response);
    }, "json");
})

function htmlBuilder(response){
    var htmlStr = "<h1>" + response.name + "</h1>"
    htmlStr += "<img src= 'http://pokeapi.co/media/img/" + response.pkdx_id + ".png'>"

    htmlStr += "<h2>Types</h2>"
    for(var i = 0; i < response.types.length; i++) {
    htmlStr += "<li>"+ response.types[i].name + "</li>"
}

    htmlStr += "<h2>Height</h2>"
    htmlStr += "<li>" + response.height + "</li>" 

    htmlStr += "<h2>Weight</h2>"
    htmlStr += "<li>" + response.weight + "</li>" 

    $('.screen').html(htmlStr)
}

    
})