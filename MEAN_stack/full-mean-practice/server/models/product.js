var mongoose = require('mongoose');
var ProductSchema = new mongoose.Schema({
    name: String,
    country_of_origin: String,
    color: String
})
mongoose.model('Product', ProductSchema);