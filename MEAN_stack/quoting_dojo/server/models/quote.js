var mongoose = require('mongoose');
var UserSchema = new mongoose.Schema({
    name: String,
    quote: String
}, {timestamps: true})
mongoose.model('User', UserSchema)