var mongoose = require('mongoose');
var Folk = mongoose.model('Folk')
module.exports = function(app){

    app.get('/', function(req, res) {
        Folk.find({}, function(err, response){
            if(err){
                res.json(err);
            }else{
                res.json(response)
            }
        })
    }),
    app.get('/new/:name', function(req,res){
        var newFolk = new Folk({name: req.params.name});
        newFolk.save(function(err){
            if(err){
                res.json(err);
            }else{
                res.redirect('/')
            }
        })
    }),
    app.get('/remove/:name', function(req,res){
        Folk.remove({name: req.params.name}, function(err, response){
            if(err){
                res.json(err);
            }else{
                res.redirect('/')
            }
        })  
    }),
    app.get('/:name', function(req,res){
        Folk.find({name: req.params.name}, function(err, response){
            if(err){
                res.json(err);
            }else{
                res.json(response)
            }
        })
    })
}