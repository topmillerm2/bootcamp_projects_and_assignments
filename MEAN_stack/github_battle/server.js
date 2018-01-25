var express= require('express');
var app = express();
var path = require('path');
var bodyParser = require('body-parser')
var session = require('express-session')

app.use(express.static(path.join(__dirname, 'public', 'dist')))

app.use(bodyParser.json({}));

app.use(session({secret: "DontTellAnybody"}));

// require('./server/config/mongoose.js');
// let routes_setter = require('./server/config/routes.js');
// routes_setter(app)

app.listen(8000, ()=>{
    console.log("on port 8000");
})