var quotes = require('../controllers/quotes.js');
module.exports = function(app){

    app.get('/', function(req, res) {
        // This is where we will retrieve the users from the database and include them in the view page we will be rendering.
        res.render('index');
    })
    // Add User Request 
    app.post('/process', function(req,res){
        quotes.create(req,res)
    })
    app.get('/quotes', function(req,res){
        quotes.show(req,res)
    })
}