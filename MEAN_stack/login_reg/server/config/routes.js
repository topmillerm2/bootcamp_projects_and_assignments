var users = require('../controllers/users.js');

module.exports = function(app){

    app.get('/', users.display),
    app.post('/process', users.create),
    app.get('/login', users.login_screen),
    app.post('/login', users.process_login),
    app.get('/main', users.main)
}