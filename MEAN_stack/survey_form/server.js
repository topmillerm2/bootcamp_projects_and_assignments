var express = require("express");
var app = express();
var bodyParser = require('body-parser');
var session = require('express-session')

app.use(bodyParser.urlencoded({ extended: true }));

app.set('view engine', 'ejs');

app.get('/', function(req, res) {
 res.render("index");
})

app.post('/process', function(req, res){
    var content = {
        name: req.body.name,
        location: req.body.location,
        language: req.body.language,
        comment: req.body.comment
    }
    
    res.render('results', {data: content})
})


app.listen(8000, function() {
 console.log("listening on port 8000");
});