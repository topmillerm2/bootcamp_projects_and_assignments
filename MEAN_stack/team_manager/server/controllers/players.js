var mongoose = require('mongoose');
var Player = mongoose.model('Player')

module.exports = {
    find: (req, res)=>{
        console.log("hit index");
        Player.find().exec((err, gotPlayers)=>{
            if(err){
                console.log("something went wrong")
                res.json(err)
            }else{
                console.log("got notes")
                res.json(gotPlayers)
                }
            })
        },
    create: (req, res)=>{
        console.log("hit create");
        console.log(req.body)
        var newPlayer = new Player(req.body);
        newPlayer.save((err)=>{
            if(err){
                console.log("something went wrong")
                res.json(err)
            }else{
                console.log("it worked!")
                res.json(newPlayer)
            }
        })
    } ,
    delete: (req, res)=>{
        console.log("hit delete");
        console.log(req.body)
        Player.remove({"_id": req.params.id}, (err, response)=>{
            if(err){
                console.log("something went wrong")
                res.json(err)
            }else{
                console.log("deleted player!")
                res.json(response)
                }
            })
    } 
}