$(document).ready(function(){

    for(var i=0; i<=440; i++){
        var url = "https://anapioficeandfire.com/api/houses/"+ i;
        house_generate(url,i);
    }

    function house_generate(url,i){
        $.get(url, function(res){
            $('#box_wrapper').append('<div class="name_box">' + '<h1 data-house="'+ i +'">' + res.name + '<button>House Details</button>'+'</h1>'+'</div>')
        }, "json");
    }

    $(document).on("click", "button",function(){ 
        var house_num = $(this).data("house");
        console.log(house_num)
        var sec_url ="https://anapioficeandfire.com/api/houses/"+ house_num;
        $.get( sec_url, function(response){
            // var titles = for(var i=0; i<response.titles[i]; i++){}
            htmlBuilder(response);
            }  , "json");
            
            function htmlBuilder(response){
            var htmlStr ='<h2>Name:</h2>' + '<p>'
            htmlStr += response.name + '</p>' + '<h2>Motto: </h2>'+'<p>'
            htmlStr += response.words +'</p>'+ '<h2>Titles:</h2>'

            for(var i=0; i<response.titles.length; i++){
            htmlStr +=  '<ul><li>'+response.titles[i]+ '</li></ul>'
            }
            $('#house_details').html(htmlStr)
            }
            // for(var i=0; i<response.titles[i]; i++){ +})
        // $('.name_box').hover(function(){
        //     $(this).animate({
        //     width: "20%",
        //     opacity: 0.4,
        //     marginLeft: "0.6in",
        //     fontSize: "3em",
        //     borderWidth: "10px"
        //     }, 1500 );
        // })

        });
    // $(document).on("hover", "#name-box", function(){
    //     $(this).css({ 
    //     width: "70%",
    //     opacity: 0.4,
    //     marginLeft: "0.6in",
    //     fontSize: "3em",
    //     borderWidth: "10px"
    //   }, 1500 );
    // })  
})
    //names, words, titles
