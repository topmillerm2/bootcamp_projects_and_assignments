
var express = require( "express");
var path = require( "path");

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
    socket.on("posting_form", function(data){
        var message = data.form;
        var number = Math.floor(Math.random()*1000)
        console.log(data.form)
        socket.emit( 'updated_message', {response: message, number: number})
    })
})