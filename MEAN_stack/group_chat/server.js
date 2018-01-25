var express = require( "express");
var path = require( "path");
var session = require("express-session")


var app = express();

app.set('views', path.join(__dirname, '/views'));
app.set('view engine', 'ejs');
app.use(session({secret: "ThisIsASecret"}));

app.get('/', function(req, res) {
 res.render("index");
})

var server = app.listen(8000, function() {
 console.log("listening on port 8000");
})
var io = require('socket.io').listen(server);
io.sockets.on('connection', function(socket){
    socket.on("posting_comment", function(data){
        var comment = data.comment;
        // session.name = data.name;
        io.emit('posted_comment', {response: comment})
    })

})