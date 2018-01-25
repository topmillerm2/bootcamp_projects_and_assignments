var mongoose = require('mongoose');
var User = mongoose.model('User')
var Bicycle = mongoose.model('Bicycle')

module.exports = {

    add: (req, res)=>{
        console.log("hit add");
        console.log(req.body.Email)
        User.find({'Email': req.body.Email}, (err, gotUser)=>{
            if (gotUser.length >0) {
                console.log("user already exists")
                req.session.userId = gotUser[0]._id;
                res.json(gotUser[0]);
            }else{
                var newUser = new User(req.body);
                newUser.save((err, savedUser)=>{
                    if(err){
                        console.log("something went wrong")
                        res.json(err)
                    }else{
                        console.log("user created")
                        req.session.userId = savedUser._id
                        console.log(req.session.userId)
                        res.json(savedUser)
                    }
                }) 
            }
        })     
    },
    create: (req, res)=>{
        console.log("hit create");
        console.log(req.session.userId)
        User.findOne({_id: req.session.userId}, (err, gotUser)=>{
            if (err) {
                console.log("couldn't find user")
                res.json(err);
            }else{
                console.log("found user")
                console.log(gotUser)
                console.log(req.body)
                var newBike = new Bicycle(req.body);
                newBike._user = req.session.userId;
                newBike.save((err)=>{
                    if(err){
                        console.log("couldn't create bike")
                        res.json(err)
                    }else{
                        console.log("saved bike, adding it to user")
                        gotUser.bicycles.push(newBike);
                        gotUser.save((err)=>{
                            if (err){
                                console.log("didn't work")
                                res.json(err);
                            }else{
                                console.log("We made it");
                                console.log(gotUser)
                                res.json(newBike)
                            }
                        })
                    }
                }) 
            }
        })     
    },
    all: (req, res)=>{
        console.log("hit all");
        console.log(req.session.userId)
        User.find({_id: req.session.userId}).populate("bicycles").exec((err, gotBikes)=>{
            if (err) {
                console.log("couldn't find bikes")
                res.json(err);
            }else{
                console.log("obtained bikes")
                res.json(gotBikes)
            }
        })
    },
    get: (req, res)=>{
        console.log("hit get");
        // console.log(req.session.userId)
        Bicycle.find({}).exec((err, gotBikes)=>{
            if (err) {
                console.log("couldn't find bikes")
                res.json(err);
            }else{
                console.log("got bikes")
                res.json(gotBikes)
            }
        })
    }
}

