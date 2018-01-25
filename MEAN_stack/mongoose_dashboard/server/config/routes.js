var elephants = require('../controllers/elephants.js');
module.exports = function(app){

    app.get('/', function(req,res){
        elephants.showAll(req,res)
    })
    // Add User Request 
    app.post('/elephant', function(req,res){
        elephants.create(req,res)
    })
    
    app.post('/process/:id', function(req,res){
        elephants.editProcess(req,res)
    })
    
    app.get('/destroy/:id', function(req,res){
        elephants.destroy(req,res)
    })

    app.get('/elephant/new', function(req, res) {
        res.render('newelephant')
        })
    
    app.get('/elephants/:id', function(req,res){
        elephants.showOne(req,res)
    })
    
    app.get('/edit/:id', function(req,res){
        elephants.edit(req,res)
    })
}