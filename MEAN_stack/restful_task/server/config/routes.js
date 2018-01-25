var tasks = require('../controllers/tasks.js');
module.exports = function(app){
    
    app.get('/', function(req,res){
        tasks.showAll(req,res)
    }),
    app.get('/:id', function(req,res){
        tasks.showOne(req,res)
    }),
    app.post('/create')
}