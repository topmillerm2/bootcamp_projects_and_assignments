var mongoose = require('mongoose');
var User = mongoose.model('User')

module.exports = {
    show: function(req, res) {
        User.find({}, function(err, users){
            if(err){
                console.log("didn't work") 
            }
                res.render('quotes', {users: users})
            })
        },
    create: function(req, res) {
        var user = new User({name: req.body.name, quote: req.body.quote});
        user.save(function(err){
            if(err){
                console.log('something went wrong');
            }else{
                console.log('success!');
                res.redirect('/quotes')
            }
        })
    }
}