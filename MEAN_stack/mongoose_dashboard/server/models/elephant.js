var mongoose = require('mongoose');
var ElephantSchema = new mongoose.Schema({
    name: String,
    country_of_origin: String,
    color: String
})
mongoose.model('Elephant', ElephantSchema);