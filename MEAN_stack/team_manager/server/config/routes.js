var Players = require('../controllers/players.js')


module.exports = (app)=>{
    app.get('/players', Players.find);
    app.post('/add/player', Players.create);
    app.delete('/delete/:id', Players.delete)

    app.all("*", (req,res,next) => {
    res.sendFile(path.resolve("./public/dist/index.html"))
    })
}