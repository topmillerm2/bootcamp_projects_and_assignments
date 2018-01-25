var express = require("express");
var app = express();
var bodyParser = require('body-parser');
var session = require('express-session');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({secret: "ThisIsASecret"}));

// app.use(express.static(path.join(__dirname, "./static")));

// app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

app.get('/', function(req, res) {
    
    if (req.session.count){
        count+=1
    }
    if (req.session.countTwo){
        counttwo +=2
    }
    else{
        count = 1
        counttwo = 1
        req.session.count = count
        req.session.countTwo = counttwo
    }
 res.render("index", {count: count, counttwo: counttwo});
})

app.post('/reset', function(req, res){
    req.session.destroy();
    res.redirect('/')
})

// app.post('/users', function(req, res) {
//  console.log("POST DATA", req.body);

//  res.redirect('/');
// })

app.listen(8000, function() {
 console.log("listening on port 8000");
});
