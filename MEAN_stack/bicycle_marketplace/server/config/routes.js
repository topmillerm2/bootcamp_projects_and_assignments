var Users = require('../controllers/users.js')
var Bicycles = require('../controllers/users.js')

module.exports = (app)=>{
    app.get('/get/bikes', Users.all);
    app.post('/add', Users.add);
    app.post('/create', Users.create);
    app.get('/get/all/bikes', Bicycles.get);
    // app.delete('/delete/:id', Players.delete)

    app.all("*", (req,res,next) => {
    res.sendFile(path.resolve("./public/dist/index.html"))
    })
}