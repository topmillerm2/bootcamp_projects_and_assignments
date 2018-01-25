var mongoose = require('mongoose');
var Note = mongoose.model('Note')

module.exports = {
    index: (req, res)=>{
        console.log("hit index");
        Note.find().sort({ createdAt: -1 }).exec((err, gotNotes)=>{
            if(err){
                console.log("something went wrong")
                res.json(err)
            }else{
                console.log("got notes")
                res.json(gotNotes)
                }
            })
        },
    create: (req, res)=>{
        console.log("hit create");
        console.log(req.body)
        var newNote = new Note(req.body);
        newNote.save((err)=>{
            if(err){
                console.log("something went wrong")
                res.json(err)
            }else{
                console.log("it worked!")
                res.json(newNote)
            }
        })
    }
}