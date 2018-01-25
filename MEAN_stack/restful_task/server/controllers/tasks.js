var mongoose = require('mongoose');
var Task = mongoose.model('Task')

module.exports = {
    showAll: function(req, res) {
        Task.find({}, function(err, tasks){
            if(err){
                res.json(err);
            }else{
                res.json({tasks})
            }
        })
    },

    showOne: function(req,res) {
        Task.find({"_id": req.params.name}, function(err,task){
            if(err){
                res.json(err);
            }else{
                res.json({task})
            }
        })
    },
    create: function(req,res){
        Task.create(request.body)
    }
}