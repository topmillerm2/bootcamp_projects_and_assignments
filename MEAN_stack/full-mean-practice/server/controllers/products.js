var mongoose = require('mongoose');
var Elephant = mongoose.model('Product')

module.exports = {
    showAll: function(req, res) {
        Elephant.find({}, function(err, elephants){
            if(err){
                console.log("Fail")
                res.json(err);
            }else{
                res.render('index', {elephants: elephants})
            }
        })
    },
    create: function(req, res) {
        console.log("POST DATA", req.body);
        var elephant = new Elephant({name: req.body.name, country_of_origin: req.body.country, color: req.body.color});
        elephant.save(function(err){
            if(err){
                console.log('something went wrong');
                res.json(err);
            }else{
                console.log('success!');
                res.redirect('/')
            }
        })
    },
    showOne: function(req, res){
        Elephant.find({"_id": req.params.id}, function(err, elephants){
            if (err){
                console.log("Failure")
            }else{
                res.render ('one_elephant', {elephants: elephants})
            }
        })
        
    },
    edit: function(req, res){
        Elephant.findOne({"_id": req.params.id}, function(err, response){
            if (err){
                console.log("Failure")
            }else{
                res.render('edit', { elephant: response})
            }
        })
        
    },
    editProcess: function(req, res) {
        // console.log("POST DATA", req.body);
        Elephant.update({"_id": req.params.id}, req.body, function(err, response) {
            if(err){
                console.log('something went wrong');
            }else{
                console.log('success!');
                res.redirect('/')
            }
        });
    },
    destroy: function(req,res){
        Elephant.remove({"_id": req.params.id}, function(err, response){
            if(err){ console.log(err)}
            else{
                res.redirect('/')
            }
        })
    }
}