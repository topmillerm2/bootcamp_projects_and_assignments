var mongoose = require('mongoose');
var User = mongoose.model('User')
var session = require('express-session')
var bcryptP = require('bcrypt-as-promised');


module.exports = {
    display: function(req, res){
        res.render('index')
    },
    
    create: function(req,res){
        var user = new User(req.body);
        var err = {};
        if(req.body.password != req.body.confirm_password){
            res.json(err)
        }else{
            user.save((err)=>{
                if(err){
                    if(err['errmsg'] != undefined){
						// errors = {
						// 	email:{ message: "Email already taken"}
						// }
						// res.json(errors);
						errors.email = { message: "Email already taken"}
					}else{
						errors = err.errors;
					}
					res.redirect('/login')
                }else{
                    res.redirect('/login')
                }
            })
        }
    },

    login_screen: function(req,res){
        res.render('login')
    },

    process_login: function(req, res){
        User.findOne({email: req.body.email}, function(err, user){
            console.log(user)
            if (user === null){
                res.json(err); 
            }           
            if (req.body.password){
                bcryptP.compare(req.body.password, user.password)
                .then(function(){
                    req.session.name = user.first_name
                    res.redirect('/main')
                })
                .catch(function(err){

                    res.json(err);
                })
            }
        })
    },

    main: function(req,res){
        res.render('main', {user: req.session.name})
    }

}
