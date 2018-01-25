var express = require( "express");
var path = require( "path");
var session = require("express-session")

var app = express();

app.set('views', path.join(__dirname, '/views'));
app.set('view engine', 'ejs');

app.get('/', function(req, res) {
 res.render("index");
})

var server = app.listen(8000, function() {
 console.log("listening on port 8000");
})
var io = require('socket.io').listen(server);
io.sockets.on('connection', function(socket){
    var count  = 0;
    socket.on("blue_clicked", function(data){
        if (data.count === "blue"){
            count  +=1
            var counter = count;
            // console.log(counter)
        }
           
        io.emit( 'updated_count', {number: counter})
    })
    socket.on("red_clicked", function(data){
        if (data.count === "red"){
            count   = 0
            var counter = count;
            console.log(counter)
        }
           
        io.emit( 'deleted_count', {number: counter})
    })
})